/import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.base import View
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
        # Won't save many-to-many fields properly without this line
        form.save_m2m()
        messages.success(self.request, "Task added")
        return redirect(todo)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddToDo, self).dispatch(*args, **kwargs)


class ToDoDetailView(DetailView):
    model = ToDoItem

    def get_context_data(self, **kwargs):
        context = super(ToDoDetailView, self).get_context_data(**kwargs)
        todo = super(ToDoDetailView, self).get_object()
        today = datetime.datetime.now().date()

        creation_date = todo.creation_date
        context["creation_date"] = creation_date

        creation_date_offset = abs(creation_date.date() - today).days > 1
        context["creation_date_offset"] = creation_date_offset

        if todo.completion_date:
            completion_date = todo.completion_date
            context["completion_date"] = completion_date

            completion_date_offset = abs(completion_date.date() - today).days > 1
            context["completion_date_offset"] = completion_date_offset
        return context


class ToDoMethodCall(View):
    """Processes incoming method calls for ToDoItem objects"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ToDoMethodCall, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        todo = ToDoItem.objects.get(pk=kwargs["pk"])
        method = kwargs["method"]
        if method == "claim":
            # This might look unnecessary, but it prevents methods without the
            # same name as their action from looking weird
            action = "claim"
        elif method == "complete":
            action = "complete"
        else:
            messages.error(self.request, "Invalid method specified")
            return redirect(todo)
        context = {"title": "{0} ToDo".format(action.capitalize()),
                   "message": "Are you sure you want to {0}\
                        <strong>{1}</strong> ?".format(action, todo.name)}
        return render(self.request, "confirm_action.html", context)

    def post(self, *args, **kwargs):
        todo = ToDoItem.objects.get(pk=kwargs["pk"])
        method = kwargs["method"]
        user = self.request.user
        if method == "claim":
            todo.claim(self.request, user)
            messages.success(self.request, "ToDo claimed")
        elif method == "complete":
            todo.complete(self.request, user)
            messages.success(self.request, "ToDo completed")
        return redirect(todo)


@login_required
def whatcanido(request):
    cando_list = ToDoItem.objects.all()
    return render(request, "todo/todoitem_list.html", {"todoitem_list": cando_list})


def tag_detail(request, tag):
    return render(request, "todo/tag_detail.html")
