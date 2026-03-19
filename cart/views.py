from .models import Cart, CartItem
from books.models import Book
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    book_id = request.data.get('book_id')
    if not book_id:
        return Response({"detail": "Book ID required"}, status=status.HTTP_400_BAD_REQUEST)
    book = Book.objects.get(id=book_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
    cart_items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def delete_from_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id, cart__user=request.user)
    except CartItem.DoesNotExist:
        return Response({"detail": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        cart_item.delete()
        return Response({"detail": "Cart item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)