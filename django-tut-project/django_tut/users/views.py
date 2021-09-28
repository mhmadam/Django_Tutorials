from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import request
from .forms import signin as signinform
import json, urllib
# Create your views here.

# signin view
def signin(request):
    
    # logout if logged in before
    logout(request)
    
    # get next url (set to '/' if None)
    valuenext = request.GET.get('next')
    if valuenext == None: valuenext = '/'

    # check request method
    if request.method == 'POST':
        
        # generate form
        form = signinform(request.POST)
        
        # check form data validation
        if form.is_valid():
            
            # get recaptcha result
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
                }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            
            # check recaptcha result
            if result['success']:
                
                # get form data
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                
                # check remember me option
                checkboxes = request.POST.getlist('remember_me')
                if 'remember_me' in checkboxes:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                
                # check user availability and login
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(valuenext)
    return render(request, 'users/signin.html', {'title':'Sign In', 'activate_signin':'active','next':valuenext})

# signup view
def signup(request):
    
    # logout if logged in before
    logout(request)
    return render(request, 'users/signup.html', {'title':'Sign Up', 'activate_signup':'active'})

# signout view
@login_required
def signout(request):
    
    # logout if logged in before
    logout(request)
    return render(request, 'users/signin.html', {'title':'Sign In', 'activate_signin':'active'})
