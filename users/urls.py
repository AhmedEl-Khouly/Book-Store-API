from django.urls import path
from .views import user_profile, admin_user_profiles

urlpatterns = [
    path('profile/', user_profile, name='user-profile'),
    path('admin/profiles/', admin_user_profiles, name='admin-user-profiles'),

]