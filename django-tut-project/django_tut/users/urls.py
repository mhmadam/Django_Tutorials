from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import signin

app_name='users'
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout')
]