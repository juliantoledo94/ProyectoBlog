from django import forms

from loginApp.models import Post

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content','status','imagen']
    
    
