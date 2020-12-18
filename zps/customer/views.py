from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Sup Yo")
# Create your views here.
