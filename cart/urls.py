from django.urls import path, include
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart",),
    path("cartitem/", views.add_to_cart, name="add_to_cart",),
    path("cartitem/<int:cart_item_id>/", views.delete_from_cart, name="delete_from_cart",),
]

