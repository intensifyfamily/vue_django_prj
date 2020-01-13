from django.shortcuts import render
from django.views import View



## Signal Analysis Controller

# extract AP-like waveform from the raw waveform
class ForExtractionView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        pass

# Determine if a waveform is an AP waveform
class FindJudgementView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        pass

# Get multiple region signal from images series
class ForMultipleView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        pass

# Get single region signal from images series
class ForSingleView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        pass

# Smooth waveform
class ForSmoothView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        pass

# LIRB waveform classification
class ForSortView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        pass

