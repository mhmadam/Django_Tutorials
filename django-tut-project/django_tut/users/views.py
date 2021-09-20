from django.db.models import fields
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.



def signin(request):
    model = User
    template_name = 'users/signin.html'
    fields = '__all__'
    if request.method == 'POST':
        if request.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            remch = request.POST.getlist('remcheck')
            print('\n\n\n', remch,'\n',username,'\n', password, '\n\n\n')
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('request.GET.next',{'mess': str(remch)})
            return render(request, 'users/signin.html', {'title':'Sign In', 'activate_signin':'active', 'mess': remch})
    return render(request, 'users/signin.html', {'title':'Sign In', 'activate_signin':'active'})

def signup(request):
    return render(request, 'users/signup.html', {'title':'Sign Up', 'activate_signup':'active'})

@login_required
def signout(request):
    logout(request)
    return render(request, 'users/signin.html', {'title':'Sign In', 'activate_signin':'active'})