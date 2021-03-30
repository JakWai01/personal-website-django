from django.shortcuts import render
from django.http import HttpResponse, Http404
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

def blogpost(request, id):
    post = Content.objects.get(id=id)

    if post.is_blog == True:
        return render(request, 'src/blogpost.html', {'content': post})
    raise Http404("This link does not lead to a blogpost.")