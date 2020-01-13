import happybase
import csv

class FileController():
    def __init__(self):
         self.conn = happybase.Connection(host='', port=9090)

    def _convert(self, data):
        if isinstance(data, bytes):  return data.decode('ascii')
        if isinstance(data, dict):   return dict(map(self._convert, data.items()))
        if isinstance(data, tuple):  return map(self._convert, data)
        return data

    def load_csv(self, rowKey):
        global information
        table = self.conn.table('h_files')
        data = self._convert(table.row(rowKey))
        information = {
            "id": data['h_info:id'],
            "environmentId": data['h_info:environmentId'],
            "softwareId": data['h_info:softwareId'],
            "imageMetaId": data['h_info:imageMetaId'],
            "iecMetaId": data['h_info:iecMetaId'],
            "name": data['h_info:name'],
            "rowKey": data['h_info:rowKey'],
            "sampleId": data['h_info:sampleId'],
            "content": list(data['h_content'])
        }
        return information

    def _send_hbase(self, filename, data):
        table = self.conn.table('h_files')
        table.put(row=filename, data=data)

    def save_csv(self, file_name, info):
        self._send_hbase(file_name, info)
        return file_name

if __name__ == '__main__':
    conn = happybase.Connection(host='', port=9090)
    name = 'h_files'
    families = {
        "h_info": dict(),
        "h_content": dict()
    }
    conn.create_table(name, families)
