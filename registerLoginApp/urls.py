from unicodedata import name
from django.urls import path
from .views import UserRegisterView



urlpatterns = [
    
    path('registerLogionApp/register/',UserRegisterView.as_view(),name='register'),
       
] 