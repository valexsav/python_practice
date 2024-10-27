from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<p>Text from the paragraph</p>")
