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
    STATUS_CHOICES = (
        ("O", "Open"),
        ("IP", "In Progress"),
        ("C", "Completed")
    )
    name = models.CharField(max_length=150)
    details = models.TextField(default="", blank=True)
    excellence = models.PositiveIntegerField(default=0)
    importance = models.IntegerField(max_length=1, choices=IMPORTANCE_CHOICES, default="0")
    due = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="O")
    completed_by = models.ForeignKey(User, blank=True, null=True, related_name='todos_completed')
    completion_date = models.DateTimeField(blank=True, null=True, editable=False)
    interests = models.ManyToManyField(Interest, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    users_claimed = models.ManyToManyField(User, blank=True, related_name='todos_claimed')
    #FIXME Currently broken. Do not use. Needs some sort of tree structure to be implemented correctly.
    sub_tasks = models.ManyToManyField("self", blank=True, related_name='parent_task')
    creator = models.ForeignKey(User, related_name='todos_created')
    creation_date = models.DateTimeField(auto_now_add=True)

    def complete(self, user):
        """Marks the item as completed and assigns it's excellence to the user"""
        if self.status != "C":
            self.status = "C"
            self.completed_by = user
            self.completion_date = datetime.now()
            self.save()
            user.userprofile.excellence += self.excellence
            user.userprofile.save()
            return True
        return False

    def claim(self, user):
        """Allows a user to claim the item"""
        if self.status != "C":
            self.status = "IP"
            self.users_claimed.add(user)
            self.save()
            return True
        return False

    def __unicode__(self):
            return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('todoitem_details', [str(self.id)])

    class Meta:
        get_latest_by = "creation_date"
        ordering = ["-creation_date"]
