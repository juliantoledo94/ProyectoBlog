from cProfile import Profile
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

from registerLoginApp.forms import SingUpForm, EditProfileForm



        





class UserRegisterView(generic.CreateView):
    form_class= SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    
class UserEditView(generic.UpdateView):
    form_class= EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
    
