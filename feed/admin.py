from django.contrib import admin
from .models import Blogpost, Project
    
# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Project)