from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.views import View

from book.models import Book

from django.core.paginator import Paginator


def pagination_test(request):
    objects_list = Book.objects.all()
    paginator = Paginator(objects_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'book/pagination_test.html',
        context={'page_obj': page_obj},
    )


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
    