from .models import Author
from .serializers import AuthorSerializer
from .permissions import IsAdminUserOrReadOnly
from books.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        author = self.get_object()
        books = author.books.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)