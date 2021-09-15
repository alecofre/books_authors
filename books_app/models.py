from django.db import models
from author_app.models import *
from .models import *
import re

# Create your models here.
class BookManager(models.Manager):
    def fields_validator(self, postData):
        JUST_LETTERS = re.compile(r'^[a-zA-Z.]+$')

        errors = {}

        if len(Book.objects.filter(title=postData['title'])) > 0:
            errors['title_exits'] = "Libro ya registrado!!!"
        else:
            if len(postData['title'].strip()) < 2 or len(postData['title'].strip()) > 50:
                errors['first_name_len'] = "Título debe tener entre 2 y 50 caracteres"

            #if not JUST_LETTERS.match(postData['title'].strip()):
            #    errors['just_letters'] = "Solo se permite el ingreso de letras en el título"
            
        return errors

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(Author, related_name='author_book', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    
    def __str__(self):
        return self.title

