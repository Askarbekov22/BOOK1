from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_1, name="book"),
    path('books/<int:id>/', views.book_2, name="books"),
    path('add-books/', views.add_book, name='add_book'),
]
