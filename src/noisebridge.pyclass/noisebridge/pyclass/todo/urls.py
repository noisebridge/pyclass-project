from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView

from pyclass.todo.models import ToDoItem
from pyclass.todo.views import AddToDo, ToDoDetailView

urlpatterns = patterns('pyclass.todo.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^details/(?P<pk>\d+)/$', ToDoDetailView.as_view(), name="todoitem_details"),
    url(r'^list/$', ListView.as_view(model=ToDoItem, paginate_by=20), name="todo_list"),
    url(r'^add/$', AddToDo.as_view(), name="add_todo"),
    url(r'^claim/(?P<pk>\d+)/$', "claim_todo", name="claim_todo"),
    url(r'^complete/(?P<pk>\d+)/$', "complete_todo", name="complete_todo"),
    url(r'^whatcanido/$', "whatcanido", name="whatcanido"),
)
