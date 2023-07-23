from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TMFO=Topic()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=Topic(request.POST)
        if TMFD.is_valid():
            return HttpResponse(str(TMFD.cleaned_data))

    return  render(request,'insert_topic.html',d)
