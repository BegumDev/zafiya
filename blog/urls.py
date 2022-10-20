from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('create_post/', views.create_post, name='create_post'),
]
