from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from books_app.models import * 

# Create your views here.
def main(request):
    context = {
        'authors': Author.objects.all().order_by('-created_at'),
    }
    return render(request, 'author_app/authors.html', context)


def add_author(request):
    #return HttpResponse('funciona')
    if request.method == 'GET':
        return redirect("/authors")
    else:
        if request.method == 'POST':
            errors = Author.objects.fields_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            request.session['level_mensaje'] = 'alert-info'
            return redirect('/authors') 
        else:
            new_first_name = request.POST['first_name']
            new_last_name = request.POST['last_name']
            new_notes = request.POST['notes']
            

            obj_author = Author.objects.create(first_name=new_first_name, last_name=new_last_name, notes=new_notes)
            obj_author.save()
    return redirect('/authors')

def info_author(request, author_id):
    author = Author.objects.get(id=author_id)
    booksbyauthor = author.author_book.all()
    books = Book.objects.all()
    context = {
        'author': author,
        'books': books,
        'booksbyauthor' : booksbyauthor,
    }
    return render(request, 'author_app/add_author.html', context)

def new_book(request, author_id):
    author = Author.objects.get(id=author_id)
    book_id = request.POST['book_id']
    #author_id = request.POST['author_id']

    book = Book.objects.get(id=book_id)
    author.author_book.add(book)
    author.save()
    return redirect(f'/authors/{author_id}')