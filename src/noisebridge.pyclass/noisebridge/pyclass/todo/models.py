from django.db import models
from django.contrib.auth.models import User
from pyclass.profiles.models import Interest


class Update(models.Model):
    """Progress updates to the ToDo item by users working on it"""
    title = models.CharField(max_length=300)
    body = models.TextField(default='', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
            return self.title

    class Meta:
        ordering = ["date"]


class Comment(models.Model):
    """Comments on the ToDo item by all users"""
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
            return self.title

    class Meta:
        ordering = ["date"]


class Tag(models.Model):
    """A descriptive item that is not necessarily an interest"""
    name = models.CharField(max_length=30)

    def __unicode__(self):
            return self.name

    class Meta:
        ordering = ["name"]


class ToDoItem(models.Model):
    IMPORTANCE_CHOICES = (
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
        ("N", "None")
    )
    name = models.CharField(max_length=150)
    details = models.TextField()
    excellence = models.PositiveIntegerField(default=0)
    due = models.DateTimeField(blank=True, null=True)
    importance = models.CharField(max_length=1, choices=IMPORTANCE_CHOICES)
    interests = models.ManyToManyField(Interest)
    tag = models.ManyToManyField(Tag)
    completed = models.BooleanField(default=False)
    users_claimed = models.ManyToManyField(User, blank=True, related_name='todos_claimed')
    sub_tasks = models.ForeignKey("self")
    comments = models.ForeignKey(Comment)
    creator = models.ForeignKey(User, blank=True, related_name='todos_created')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
            return self.name

    class Meta:
        ordering = ["name"]
