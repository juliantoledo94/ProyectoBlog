
from django.urls import path,include
from .views import login, PostList, DetailView



urlpatterns = [
    #path("",login,name="home"),
    path('',PostList.as_view(),name="home"),
    path('<slug:slug>/', DetailView.as_view(), name="post_detail"),
    
] 
