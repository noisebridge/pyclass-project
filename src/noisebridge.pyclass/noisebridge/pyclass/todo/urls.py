from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from pyclass.todo.models import ToDoItem

urlpatterns = patterns('pyclass.todo.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^details/(?P<pk>\d+)/$', DetailView.as_view(model=ToDoItem), name="todoitem_details"),
    url(r'^list/$', ListView.as_view(model=ToDoItem, paginate_by=20)),
)
