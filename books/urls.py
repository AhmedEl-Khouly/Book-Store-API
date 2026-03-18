from django.urls import path, include
from . import views

urlpatterns = [
    # Book GET URLs for listing and detail views (available to all users)
    path("books/", views.book_list, name='books-list'),
    # Book GET URL by id for detail views (available to all users)
    path("books/<int:id>/", views.book_detail, name='books-detail'),
    # Book POST URL for creating a new book (admins only)
    path("books/create/", views.book_create, name='books-create'),
    # Book PUT, PATCH, DELETE URL for updating, deleting a book (admins only)
    path("books/update/delete/<int:id>/", views.book_update_delete, name='books-update'),
]