from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView

from pyclass.todo.models import ToDoItem
from pyclass.todo.views import AddToDo, ToDoDetailView, ToDoMethodCall

urlpatterns = patterns('pyclass.todo.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^details/(?P<pk>\d+)/$', ToDoDetailView.as_view(), name="todoitem_details"),
    url(r'^list/$', ListView.as_view(model=ToDoItem, paginate_by=20), name="todo_list"),
    url(r'^add/$', AddToDo.as_view(), name="add_todo"),
    url(r'^methods/(?P<pk>\d+)/(?P<method>\w+)/$', ToDoMethodCall.as_view(), name="todoitem_methods"),
    url(r'^whatcanido/$', "whatcanido", name="whatcanido"),
)
