
from unicodedata import name
from django.urls import path,include
from .views import *  
from loginApp import views



urlpatterns = [
    #path("",login,name="home"),
    
    path('',PostList.as_view(),name="home"),
    path('post/crear', Crear_post,name="crear_post"),
    path('buscarTitle',busqueda_blog,name="busqueda"),
    path('buscar/',buscar,name='buscar'),
    
    path('<slug:slug>/', DetailView.as_view(), name="post_detail"),
    
    
] 
