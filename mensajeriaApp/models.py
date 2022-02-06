from django.db import models
from loginApp.models import Post
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return '%s - %s' % (self.post.title , self.name)