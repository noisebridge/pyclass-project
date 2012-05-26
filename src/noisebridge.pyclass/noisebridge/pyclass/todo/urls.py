from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from pyclass.todo.models import ToDoItem

urlpatterns = patterns('pyclass.todo.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^details/(?P<pk>\d+)/$', DetailView.as_view(
        model=ToDoItem,
        context_object_name="todoitem",
    )),

)
