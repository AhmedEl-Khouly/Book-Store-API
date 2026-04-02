from rest_framework import serializers
from books.serializers import BookSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ["id","book", "quantity", "total_price"]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ["user", "created_at", "total_cart_price", "items"]

