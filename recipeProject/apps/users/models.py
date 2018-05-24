from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

class ProfileManager(models.Manager):
    def after_user_signed_up(sender, request, user):
        result = True
        return result

class Profile(models.Model):
    username = models.CharField(max_length=25, blank = True)
    OAuth_info = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProfileManager()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(OAuth_info=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()