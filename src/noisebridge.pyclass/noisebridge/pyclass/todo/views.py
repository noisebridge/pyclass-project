from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from pyclass.todo.models import ToDoItem
from pyclass.todo.forms import ToDoItemForm


class AddToDo(CreateView):
    model = ToDoItem
    form_class = ToDoItemForm

    def form_valid(self, form):
        todo = form.save(commit=False)
        # Must be passed to populate the "creator" field, which is required.
        todo.save(self.request.user)
        messages.success(self.request, "Task added")
        return redirect(todo)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddToDo, self).dispatch(*args, **kwargs)

