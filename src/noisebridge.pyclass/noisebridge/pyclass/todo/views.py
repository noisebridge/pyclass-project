from django.shortcuts import render, redirect
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
        form.save_m2m()
        messages.success(self.request, "Task added")
        return redirect(todo)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddToDo, self).dispatch(*args, **kwargs)


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
