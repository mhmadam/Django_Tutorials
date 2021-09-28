from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.

# blog home view
def home(request):
    return render(request, 'blog/home.html', {'title':'Blog-Home', 'activate_home':'active'})

# blog about view (login_required for test)
@login_required
def about(request):
    return render(request, 'blog/about.html', {'title':'Blog-About', 'activate_about':'active'})
