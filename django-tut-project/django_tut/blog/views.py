from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .decorators import authenticate_user, testdecor

# Create your views here.

# blog home view
@testdecor(url='home')
def home(request):
    context = {'title':'Blog-Home', 'activate_home':'active'}
    return render(request, 'blog/home.html', context)

# blog about view (login_required for test)

def about(request):
    context = {'title':'Blog-About', 'activate_about':'active'}
    return render(request, 'blog/about.html', context)
