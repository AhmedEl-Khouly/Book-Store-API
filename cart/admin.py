from django.contrib import admin
from .models import Cart, CartItem

admin.site.site_header = "Bookstore Admin"
admin.site.site_title = "Bookstore Admin Portal"
admin.site.index_title = "Welcome to Bookstore Admin Portal"

admin.site.register(Cart)
admin.site.register(CartItem)