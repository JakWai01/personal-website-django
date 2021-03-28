from django.shortcuts import render
from django.http import HttpResponse
from .models import Content

# Create your views here.
def index(request):

    content = Content.objects.all().order_by('date')
    return render(request, 'feed/feed.html', {'content':content})
