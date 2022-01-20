from unicodedata import name
from django.urls import path,include
from .views import login


urlpatterns = [
    path("",login,name="home")
] 
