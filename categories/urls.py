from django.urls import path, include
from . import views

urlpatterns = [
    # Category GET URLs for listing and detail views (available to all users)
    path('categories/', views.category_list, name='category-list'),
    # Category GET and POST URL for creating a new category (admins only)
    path('categories/create/', views.category_create, name='category-create'),
    # Category GET URL by slug for detail views (available to all users)
    # Category PUT, DELETE URL by slug for updating and deleting a category (admins only)
    path('categories/<slug:slug>/', views.category_update_delete, name='category-detail'),

]

