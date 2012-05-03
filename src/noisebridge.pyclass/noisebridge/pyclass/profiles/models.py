from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    biography = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        ordering = ["user"]


class Interest(models.Model):
    user = models.ManyToManyField(UserProfile)
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
