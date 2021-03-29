from django.shortcuts import render
from django.http import HttpResponse
from .models import Content

# Create your views here.
def index(request):
    content = Content.objects.all().order_by('date').reverse()
    return render(request, 'src/feed.html', {'content': content})

def blog(request):
    content = Content.objects.filter(is_blog=True).order_by('date').reverse()
    return render(request, 'src/feed.html', {'content': content})

def projects(request):
    content = Content.objects.filter(is_blog=False).order_by('date').reverse()
    return render(request, 'src/feed.html', {'content': content})