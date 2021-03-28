from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length = 255)
    date = models.DateField(auto_created=True)
    abstract = models.CharField(max_length = 1023)
    text = models.CharField(max_length = 8191)

class Project():
    title = models.CharField(max_length = 255)
    date = models.DateField(auto_created=True)
    abstract = models.CharField(max_length = 1023)