from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/logout/', UserLogoutView.as_view(), name='user-logout'),
]