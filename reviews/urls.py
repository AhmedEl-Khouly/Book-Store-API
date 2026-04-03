from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from books.views import BookViewSet
from .views import ReviewViewSet

# router = DefaultRouter()
# router.register('reviews', ReviewViewSet, basename='review')

router = routers.SimpleRouter()
router.register(r'books', BookViewSet, basename='review')

books_router = routers.NestedSimpleRouter(router, r'books', lookup='book')
books_router.register(r'reviews', ReviewViewSet, basename='book-reviews')


urlpatterns = [
    # path('', include(router.urls)),
    path('',include(router.urls + books_router.urls,))
]
