from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = "__all__"