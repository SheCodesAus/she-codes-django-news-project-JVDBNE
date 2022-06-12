from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import login
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import ListView
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import CustomUser
from news.models import NewsStory
from .forms import CustomUserCreationForm

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        f=super().form_valid(form)
        user = self.object
        login(self.request, user)
        return f


class AuthorsView(ListView):
    model = CustomUser
    template_name = 'users/viewAuthors.html'
    

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = CustomUser.objects.all()
        return 