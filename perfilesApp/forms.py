from loginApp.models import Profile
from django import forms

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('bio','profile_pic','website_url','facebook_url','instagram_url')
        
        
        
        widgets = {
            'bio':forms.Textarea(attrs={'class': 'form-control'}),
            #'profile_pic':forms.TextInput(attrs=""),
            'website_url':forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class': 'form-control'}),
            
        }