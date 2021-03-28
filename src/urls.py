from django.contrib import admin
from django.urls import path, include
from .views import index, blog, projects

urlpatterns = [
    path('', index, name='index'),
    path('blog', blog, name='blog'),
    path('projects', projects, name='projects')
]