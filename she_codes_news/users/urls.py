from django.urls import path
from .views import CreateAccountView, EditUserProfileView, UserProfileView, AuthorsView
from . import views


app_name = 'users'

urlpatterns = [
    path('createAccount/', CreateAccountView.as_view(), name='createAccount'),
    path('edit-profile/', EditUserProfileView.as_view(), name='editProfile'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('view-authors', AuthorsView.as_view(), name='authors'),
]