from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'posts'
urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete/<str:pk>/', views.delete_post, name='delete_post'),
]