from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *


# Create your views here.
def home(request):
    context = {
        'books': Book.objects.all().order_by('-created_at'),
    }
    return render(request, 'books_app/home.html', context)

    

def add_book(request):
    #return HttpResponse('funciona')
    if request.method == 'GET':
        return redirect("/add_book")
    else:
        if request.method == 'POST':
            errors = Book.objects.fields_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            request.session['level_mensaje'] = 'alert-info'
            return redirect('/') 
        else:
            new_title = request.POST['title']
            new_description = request.POST['description']
            

            obj_book = Book.objects.create(title=new_title, description=new_description)
            obj_book.save()
    return redirect('/')
    
 
def info_book(request, book_id):
    book = Book.objects.get(id=book_id)
    authors = Author.objects.all()
    context = {
        'book': book,
        'authors': authors
    }
    return render(request, 'books_app/books.html', context)

def new_author(request, book_id):
    #book_id = request.POST['book_id']
    author_id = request.POST['author_id']

    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    book.author = author
    book.save()
    return redirect(f'/books/{book_id}')
    