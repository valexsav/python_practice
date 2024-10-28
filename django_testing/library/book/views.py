from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.views import View

from book.models import Book


def index(request):
    books = Book.objects.all()
    return render(
        request,
        'book/index.html',
        context={'books': books},
    )

def get_book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    return render(
        request,
        'book/book_info.html',
        context={'book': book},
    )


def redirect_to_main_page(request):
    return redirect('index')

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<p>Hello, World GET</p>")
    
    def post(self, request):
        return HttpResponse("<p>Hello, World POST</p>")
    