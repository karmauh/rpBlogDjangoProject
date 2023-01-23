from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default=None, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='root')
    body = models.TextField()
    snippet = models.TextField(max_length=255)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('post_details', args=(str(self.id)))
        return reverse('home')
    