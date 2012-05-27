from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings


class Interest(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('interest_details', [str(self.id)])

    class Meta:
        ordering = ["name"]


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="avatars",
                               default=settings.STATIC_URL + "default-avatar.png")
    biography = models.TextField(default='', blank=True)
    interests = models.ManyToManyField(Interest)
    excellence = models.PositiveIntegerField(default=0)

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
