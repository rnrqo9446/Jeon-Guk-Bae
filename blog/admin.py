from django.contrib import admin
from .models import Post
from django.urls import path
import blog.views
# Register your models here.
admin.site.register(Post)

