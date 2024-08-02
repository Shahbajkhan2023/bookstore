from django.urls import path
from .views import book_list, author_list

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('authors/', author_list, name='author_list'),
   
]
