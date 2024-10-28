"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from book.views import (
    index,
    HelloWorldView,
    get_book_details,
    redirect_to_main_page,
    pagination_test,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('function/', index, name='index'),
    path('book/<int:book_id>', get_book_details, name='book_details'),
    path('class/', HelloWorldView.as_view()),
    path('', redirect_to_main_page),
    path('pagination/', pagination_test, name='pagination_test'),
]
