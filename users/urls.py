from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin to view all user profiles
    path('admin/profiles/', admin_user_profiles, name='admin-user-profiles'),
    # Authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Refresh token endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # User registration and profile management
    path('register/', register, name='register'),
    # User profile endpoints
    path('profile/', user_profile, name='user-profile'),
    # Update user profile endpoint
    path('profile/update/', update_profile, name='update-profile'),
]