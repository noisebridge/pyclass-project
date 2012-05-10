from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from pyclass.profiles.models import Interest
from pyclass.profiles.forms import SearchInterestForm, AddInterestForm


def search_interests(request):
    """
    Returns a list with all interests that contain (case insensitive) the string "query".
    """
    if "query" in request.GET:
        form = SearchInterestForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            interests = Interest.objects.filter(name__icontains=query)
            return render_to_response("search_results.html",
                {"interests": interests, "query": query})
    else:
        form = SearchInterestForm()
    return render_to_response("search_form.html", {"form": form})


@login_required
def add_interests(request):
    """
    Adds a new interest from user to database
    """
    if request.method == "POST":
        form = AddInterestForm(request.POST)
        if form.is_valid():
            i = Interest(name=form.cleaned_data["interest"])
            i.save()
            return HttpResponseRedirect("interest_submitted.html")
    else:
        form = AddInterestForm()
    return render_to_response("addinterest.html", {"form": form}, context_instance=RequestContext(request))


def interest_submitted(request):
    return render_to_response("interest_submitted.html")
