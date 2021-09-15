from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/add_author', views.add_author, name='add_author'),
    path('/<author_id>', views.info_author, name='info_author'),
    path('/<author_id>/new_book', views.new_book, name='new_book'),
]
