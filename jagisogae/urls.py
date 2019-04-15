from django.contrib import admin
from django.urls import path, include
import blog.views
import jagisogae.views

urlpatterns = [
    # path('blog/', include('blog.urls')),
    # # path('blog/home/', blog.views.home, name = 'home'),
    # # path('blog/home/post/<int:post_id>/', blog.views.detail, name = 'detail'),
    # # # post마다 특정한 숫자가 저절로 들어가게 된다!!!!
    # # path('blog/post/new/', blog.views.post_new, name = 'new'),
    # path('jagisogae/', include('jagisogae.urls')),
    path('home', jagisogae.views.jagisogae_home, name = 'jagisogae_home'),
    path('detail', jagisogae.views.jagisogae_detail, name = 'jagisogae_detail' )
    
]
