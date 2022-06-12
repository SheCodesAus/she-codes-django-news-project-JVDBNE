from django.urls import path
from .views import CreateAccountView, AuthorsView
from . import views


app_name = 'users'

urlpatterns = [
    path('createAccount/', CreateAccountView.as_view(), name='createAccount'),
    path('view-authors', AuthorsView.as_view(), name='authors'),
]