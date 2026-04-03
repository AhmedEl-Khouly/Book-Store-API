from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs.get('book_pk')
        if book_id:
            return Review.objects.filter(book_id=book_id)
        return Review.objects.all()
    
    def perform_create(self, serializer):
        book_id = self.kwargs.get('book_pk')
        serializer.save(user=self.request.user, book_id=book_id)
