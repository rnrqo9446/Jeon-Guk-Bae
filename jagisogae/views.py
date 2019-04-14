from django.shortcuts import render

# Create your views here.

def jagisogae_home(request):
    return render(request, 'jagisogae/home.html')

def jagisogae_detail(request):
    return render(request, 'jagisogae/detail.html')
