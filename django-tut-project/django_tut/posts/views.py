from django.shortcuts import redirect, render
from .models import Post
from .forms import CreatePostForm
from django.core.paginator import Paginator


# Create your views here.

def post_list(request):
    titl = request.GET.get('title')
    if titl:
        posts = Post.objects.filter(title__contains=titl).order_by('-id')
    elif titl == None:
        titl = ''
        posts = Post.objects.all().order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
    print(titl)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts':posts,'srch_holder':titl, 'title':'Post list', 'activate_home':'active'}
    return render(request, 'posts/post_list.html', context)

def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else:
        form = CreatePostForm()
    context = {'form':CreatePostForm}
    return render(request, 'posts/create_post.html', context)

def delete_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
    return redirect('posts:post_list')