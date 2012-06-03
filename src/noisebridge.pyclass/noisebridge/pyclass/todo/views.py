import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
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


@login_required
def claim_todo(request, pk):
    todo = ToDoItem.objects.get(id=pk)
    if request.method == "POST":
        user = request.user
        todo.claim(request, user)
        messages.success(request, "ToDo claimed")
        return redirect(user)
    return render(request, "confirm_action.html",
                 {"title": "Claim ToDo",
                 "message": "Are you sure you want to claim '" + todo.name + "'' ?"
    })


@login_required
def complete_todo(request, pk):
    todo = ToDoItem.objects.get(id=pk)
    if request.method == "POST":
        user = request.user
        todo.complete(request, user)
        messages.success(request, "ToDo completed")
        return redirect(user)
    return render(request, "confirm_action.html",
                 {"title": "Complete ToDo",
                 "message": "Are you sure you want to complete '" + todo.name + "'' ?"
    })


@login_required
def whatcanido(request):
    cando_list = ToDoItem.objects.all()
    return render(request, "todo/todoitem_list.html", {"todoitem_list": cando_list})
