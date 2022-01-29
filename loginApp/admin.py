from django.contrib import admin

# Register your models here.
from .models import Post , Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter= ("status",)
    searh_fields= ["title", "content"]



admin.site.register(Post, PostAdmin)
admin.site.register(Profile)