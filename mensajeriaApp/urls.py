
from django.urls import path,include

from .views import AddCommentView


#from mensajeriaApp.views import Bandeja_entrada





urlpatterns = [
      
    path('article/<int:pk>/comment',AddCommentView.as_view(),name='add_comment')
    
] 