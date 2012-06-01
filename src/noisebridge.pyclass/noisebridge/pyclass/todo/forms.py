from django import forms

from pyclass.todo.models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ("name", "details", "excellence", "importance", "due", "interests", "tags")
