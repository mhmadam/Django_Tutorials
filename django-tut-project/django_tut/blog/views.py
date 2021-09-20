from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {'title':'Blog-Home', 'activate_home':'active'})

@login_required
def about(request):
    if request.method == 'POST':
        remch = request.POST.getlist('car')
        print('\n\n\n', remch, '\n\n\n')
        return render(request, 'blog/about.html', {'title':'Sign In', 'activate_signin':'active', 'mess': remch})
    return render(request, 'blog/about.html', {'title':'Blog-About', 'activate_about':'active'})
