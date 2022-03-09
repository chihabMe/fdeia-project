

from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title  = models.CharField(max_length=140)
    body = models.TextField()
    
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',related_name='tags')
    likes = models.ManyToManyField(User,related_name='post_likes')
    slug = models.SlugField(blank=True,null=True)
    date = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField( auto_now=True, auto_now_add=False)

    def get_likes_count(self):
        return self.likes.count()
    def get_comments_count(self):
        return self.post_comments.count()
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    def save(self,*args, **kwargs ):
        if not self.slug:
            self.title  = self.user.username+self.body[0:30]
            self.slug = slugify(self.title) 
        super(Post,self).save(*args, **kwargs)
    def __str__(self) :
        return self.title
    class Meta:
        ordering =('-date','-update')
class Tag(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField( auto_now=True, auto_now_add=False)
    def __str__(self) :
        return self.title
class Comment(models.Model):
    body = models.CharField(max_length=300)
    date = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField( auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User,related_name='user_comments',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='post_comments',on_delete=models.CASCADE)
    def __str__(self) :
        return self.title