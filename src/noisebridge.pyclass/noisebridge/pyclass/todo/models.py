from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from pyclass.profiles.models import Interest


class Tag(models.Model):
    """A descriptive item that is not necessarily an interest"""
    name = models.CharField(max_length=30)

    def __unicode__(self):
            return self.name

    class Meta:
        ordering = ["name"]


class ToDoItem(models.Model):
    IMPORTANCE_CHOICES = (
        (3, "High"),
        (2, "Medium"),
        (1, "Low"),
        (0, "None")
    )
    name = models.CharField(max_length=150)
    details = models.TextField(default="", blank=True)
    excellence = models.PositiveIntegerField(default=0)
    importance = models.IntegerField(max_length=1, choices=IMPORTANCE_CHOICES, default="0")
    due = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_by = models.ForeignKey(User, blank=True, null=True, related_name='todos_completed')
    completion_date = models.DateTimeField(blank=True, null=True, editable=False)
    interests = models.ManyToManyField(Interest, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    users_claimed = models.ManyToManyField(User, blank=True, related_name='todos_claimed')
    sub_tasks = models.ManyToManyField("self", blank=True, related_name='parent_task')
    creator = models.ForeignKey(User, related_name='todos_created')
    creation_date = models.DateTimeField(auto_now_add=True)

    def complete(self, user):
        """Marks the item as completed and assigns it's excellence to the user"""
        self.completed = True
        self.completed_by = user
        self.completion_date = datetime.now()
        self.save()
        user.userprofile.excellence += self.excellence
        user.userprofile.save()

    def __unicode__(self):
            return self.name

    class Meta:
        get_latest_by = "creation_date"
        ordering = ["-creation_date"]


class Update(models.Model):
    """Progress updates to the ToDo item by users working on it"""
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    todoitem = models.ForeignKey(ToDoItem, verbose_name=u'update about')

    def __unicode__(self):
            return self.title

    class Meta:
        get_latest_by = "date"
        order_with_respect_to = "todoitem"
        ordering = ["-date"]


class Comment(models.Model):
    """Comments on the ToDo item by all users"""
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    todoitem = models.ForeignKey(ToDoItem, verbose_name=u'comment on')

    def __unicode__(self):
            return self.title

    class Meta:
        get_latest_by = "date"
        order_with_respect_to = "todoitem"
        ordering = ["-date"]
