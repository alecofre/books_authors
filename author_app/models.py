from django.db import models
import re

# Create your models here.
class AuthorManager(models.Manager):
    def fields_validator(self, postData):
        JUST_LETTERS = re.compile(r'^[a-zA-Z.]+$')

        errors = {}

        if Author.objects.filter(last_name = postData['last_name']).filter(first_name = postData['first_name']):
                errors['author_exists'] = "Autor ya existe"
        
        else:
            if len(postData['first_name'].strip()) < 2 or len(postData['first_name'].strip()) > 30:
                errors['first_name_len'] = "Nombre debe tener entre 2 y 30 caracteres"

            if len(postData['last_name'].strip()) < 2 or len(postData['last_name'].strip()) > 30:
                errors['last_name_len'] = "Apellido debe tener entre 2 y 30 caracteres"

            if not JUST_LETTERS.match(postData['first_name']) or not JUST_LETTERS.match(postData['last_name']):
                errors['just_letters'] = "Solo se permite el ingreso de letras en el nombre y apellido"
            
        return errors
        

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, unique=True)
    notes = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name



