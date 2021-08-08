from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('ab', views.about, name='blog-about'),
]