from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Interest(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    biography = models.TextField(default='', blank=True)
    interest = models.ManyToManyField(Interest)

    def __unicode__(self):
        return self.user.username

    class Meta:
        ordering = ["user"]


def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
