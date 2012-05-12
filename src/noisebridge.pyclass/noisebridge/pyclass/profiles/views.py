from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from pyclass.profiles.models import Interest, UserProfile
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
    return render_to_response("search_form.html", {"form": form},
                             context_instance=RequestContext(request))


@login_required
def add_interests(request):
    """
    Adds an interest to the user's profile. If it doesn't exist, adds it to database first.
    """
    if request.method == "POST":
        form = AddInterestForm(request.POST)
        if form.is_valid():
            i = form.cleaned_data["interest"]
            interest_list = Interest.objects.filter(name=i).count()
            if not interest_list:
                interest = Interest(name=i)
                interest.save()
            else:
                interest = Interest.objects.get(name=i)
            profile = UserProfile.objects.get(user=request.user)
            profile.interest.add(interest)
            profile.save()
            return HttpResponseRedirect("interest_submitted.html")
    else:
        form = AddInterestForm()
    return render_to_response("addinterest.html", {"form": form},
                             context_instance=RequestContext(request))


def interest_submitted(request):
    return render_to_response("interest_submitted.html")


@login_required
def display_avatar(request):
    profile = UserProfile.objects.get(user=request.user)
    return render_to_response("display_avatar.html", {"profile": profile},
                             context_instance=RequestContext(request))
