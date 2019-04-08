"""gukbae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/home/', blog.views.home, name = 'home'),
    path('blog/home/post/<int:post_id>/', blog.views.detail, name = 'detail'),
    # post마다 특정한 숫자가 저절로 들어가게 된다!!!!
    path('blog/post/new/', blog.views.post_new, name = 'new')
]
# path 앞에 주소 적는거 잊지 말아라!!!!
