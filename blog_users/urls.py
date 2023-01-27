from django.urls import path
from .views import UserRegisterView, UserChangeView, PasswordsChangeView, ShowProfilePageView, EditCharacterView, CreateCharacterView, ShowOtherProfilePageView
from . import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserChangeView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile'),
    path('<int:pk>/edit_character/', EditCharacterView.as_view(), name='edit_character'),
    path('create_charcter/', CreateCharacterView.as_view(), name='create_character'),
    path('all_profiles/', ShowOtherProfilePageView, name='all_profiles'),
]
