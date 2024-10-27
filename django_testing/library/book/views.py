from django.shortcuts import (
    render,
    redirect,
)
from django.http import HttpResponse
from django.views import View

from book.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})

def get_book_details(request, book_id):
    
    book = Book.objects.get(id=book_id)
    return render(request, 'book/book_info.html', {'book': book})


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<p>Hello, World GET</p>")
    
    def post(self, request):
        return HttpResponse("<p>Hello, World POST</p>")
    