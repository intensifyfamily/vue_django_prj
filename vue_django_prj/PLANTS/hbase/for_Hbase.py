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

    def load_csv(self, files_name, line):
        global information
        table = self.conn.table('h_files')
        q = 0
        for filename in files_name:
            data = self._convert(table.row(filename))
            information = {
                "id": data['h_info:id'],
                "environmentId": data['h_info:environmentId'],
                "softwareId": data['h_info:softwareId'],
                "imageMetaId": data['h_info:imageMetaId'],
                "iecMetaId": data['h_info:iecMetaId'],
                "name": data['h_info:name'],
                "rowKey": filename,
                "sampleId": data['h_info:sampleId']
            }
            rows = []
            for i in range(1, line[0]):
                rows.append(eval(data['h_content:'+str(i)].replace(" ","")))
            with open('/var/www/html/PLANTS/files/' + filename, 'w', encoding='utf-8-sig')as f:
                f_csv = csv.writer(f)
                f_csv.writerows(rows)
            q = q + 1
        return information

    def _send_hbase(self, filename, data):
        table = self.conn.table('h_files')
        table.put(row=filename, data=data)

    def save_csv(self, file_name, information):
        csv_file=csv.reader(open('/var/www/html/PLANTS/files/' + file_name,'r', encoding='utf-8-sig'))
        data = {}
        head = []
        i = 1
        for line in csv_file:
            print(str(line))
            data.update({'h_content:'+str(i): str(line)})
            i = i + 1
        data.update(information)
        self._send_hbase(file_name, data)
        return i
    def delete_csv(self, rowKey):
        table = self.conn.table('h_files')
        table.delete(rowKey)
        return "OK"
    def search_data(self, rowKey):
        table = self.conn.table('h-files')
        data = self._convert(table.row(rowKey))
        rows = []
        for i in range(1, len(data) + 1):
            try:
                rows.append(eval(data['h_content:' + str(i)].replace(" ", "")))
            except:
                break
        return str(rows)
if __name__ == '__main__':
    conn = happybase.Connection(host='', port=9090)
    name = 'h_files'
    families = {
        "h_info": dict(),
        "h_content": dict()
    }
    conn.create_table(name, families)
