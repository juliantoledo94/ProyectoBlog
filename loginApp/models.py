
from audioop import reverse
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

STATUS =((0,"Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, )
    slug = models.SlugField(max_length=200, )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    created_on= models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now_add=True)
    content= RichTextField(blank=True, null= True)
    #content= models.TextField()
    status=models.IntegerField(choices=STATUS, default=0)
    imagen=models.ImageField(upload_to="fotos", null= True,  blank=True)
    
    
class Meta:
    ordering = ["-created_on"]
    
def __str__(self):
    return self.title


class Profile(models.Model):
    user = models.OneToOneField(User,null= True, on_delete= models.CASCADE)
    bio= models.TextField()
    profile_pic = models.ImageField(upload_to="fotos", null= True,  blank=True)
    website_url = models.CharField(max_length=200,null= True,  blank=True )
    facebook_url = models.CharField(max_length=200,null= True,  blank=True )
    instagram_url = models.CharField(max_length=200,null= True,  blank=True )
    
    def __str__(self):
        return str(self.user)
    
 
    
    
