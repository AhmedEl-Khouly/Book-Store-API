from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/users/', include('users.urls')),
    # path('api/books/', include('books.urls')),
    # path('api/authors/', include('authors.urls')),
    # path('api/cart/', include('cart.urls')),
    # path('api/categories/', include('categories.urls')),
    # path('api/reviews/', include('reviews.urls')),
]
