from distutils.command.upload import upload
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User 
# Create your models here.
def namer (instance ,filename):
    name  = instance.user.username+"/"+filename
    return name 
class Profile(models.Model):
    bio = models.TextField(blank=True,null=True)
    image  = models.ImageField(upload_to=namer,blank=True,null=True)
    user  = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
