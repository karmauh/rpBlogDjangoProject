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
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    appearance = models.TextField()
    history = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)