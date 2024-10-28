from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'biodata.html')

def about(request):
    return HttpResponse("ini adalah halama index")