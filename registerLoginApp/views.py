from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

from registerLoginApp.forms import SingUpForm


class UserRegisterView(generic.CreateView):
    form_class= SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    
# class UserEditView(generic.CreateView):
#     form_class= UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')
    