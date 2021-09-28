from django.shortcuts import render


posts = [
	{
		'author':'Amin',
		'title':'Blog post 1',
		'content':'First post content',
		'date_posted':'August 27, 2018'
	},
	{
		'author':'Mohammad',
		'title':'Blog post 2',
		'content':'second post content',
		'date_posted':'August 29, 2018'
	}
]
# Create your views here.
def home(request):
	context = {
		'posts':posts,
		'title':'Home'
	}
	return render(request,'blog/home.html',context)
def about(request):
	return render(request,'blog/about.html',{'content':'About Blog','title':'About'})
