from django.contrib import admin
from django.urls import path
import blog.views
import jagisogae.views

urlpatterns = [
    path('home/', blog.views.home, name = 'home'),
    path('post/<int:post_id>/', blog.views.detail, name = 'detail'),
    # post마다 특정한 숫자가 저절로 들어가게 된다!!!!
    path('post/new/', blog.views.post_new, name = 'new'),
    path('post/<int:post_id>/edit', blog.views.post_edit, name = 'edit'),
    path('post/<int:post_id>/delete', blog.views.post_delete, name = 'delete'),
]
