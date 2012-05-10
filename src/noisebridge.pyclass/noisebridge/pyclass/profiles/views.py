from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from pyclass.profiles.models import Interest
from pyclass.profiles.forms import SearchInterestForm, AddInterestForm
from django.views.decorators.csrf import csrf_exempt


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


#NOTE: blocks csrf, get function working correctly with csrf and then remove
@csrf_exempt
def add_interests(request):
    """
    Adds a new interest from user to database
    """
    if request.method == "POST":
        form = AddInterestForm(request.POST)
        if form.is_valid():
            i = Interest(name=form.cleaned_data["interest"])
            i.save()
            # FIXME: when passing {"interest": i} throws TypeError (claims 3 args, wants 2)
            return HttpResponseRedirect("interest_submitted.html")
    else:
        form = AddInterestForm()
    csrf_request = {}
    csrf_request.update(csrf(request))
    #FIXME: passing csrf_request to args throws TypeError "pop expected at least 1 arguments, got 0"
    return render_to_response("addinterest.html", {"form": form})


def interest_submitted(request):
    return render_to_response("interest_submitted.html")
