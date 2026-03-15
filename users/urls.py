from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/profiles/', admin_user_profiles, name='admin-user-profiles'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', user_profile, name='user-profile'),
    path('profile/register/', register, name='register'),
    path('profile/update/', update_profile, name='update-profile'),
]        