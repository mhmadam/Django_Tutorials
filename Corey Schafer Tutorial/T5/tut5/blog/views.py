from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
	context = {
		'posts':Post.objects.all(),
		'title':'Home'
	}
	return render(request,'blog/home.html',context)
def about(request):
	return render(request,'blog/about.html',{'content':'About Blog','title':'About'})