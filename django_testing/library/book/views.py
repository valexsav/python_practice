from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def index(request):
    if request.method == "POST":
        return HttpResponse("<p>Hello, World POST</p>")
    return HttpResponse("<p>Hello, World GET</p>")


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<p>Hello, World GET</p>")
    
    def post(self, request):
        return HttpResponse("<p>Hello, World POST</p>")
    