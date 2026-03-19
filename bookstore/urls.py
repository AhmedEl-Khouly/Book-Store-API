from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("categories.urls")),
    path("api/", include("books.urls")),
    path("api/", include("cart.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)