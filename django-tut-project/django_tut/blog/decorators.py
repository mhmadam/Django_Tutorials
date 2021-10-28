from django.shortcuts import redirect

def authenticate_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            print('unauthenticate user')
            return redirect('blog:home')
    return wrapper_func

def testdecor(url=''):
    def decor(view_func):
        def wrapper_func(request, *args, **kwargs):
            print(url)
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decor