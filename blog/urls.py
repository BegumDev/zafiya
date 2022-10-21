from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('create_post/', views.create_post, name='create_post'),
    path('read_post/<int:id>', views.read_post, name='read_post'),
    path('update_post/<int:id>', views.update_post, name='update_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
]
