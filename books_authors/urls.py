"""books_authors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from books_app import views

urlpatterns = [
    path('', include('books_app.urls')),
    path('authors', include('author_app.urls')),
    path('books/<book_id>', views.info_book, name='info_book'),
    path('books/<book_id>/new_author', views.new_author, name='new_author'),
    path('admin/', admin.site.urls),
]
