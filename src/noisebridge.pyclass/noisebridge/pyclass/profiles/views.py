from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pyclass.profiles.models import Interest, UserProfile
from pyclass.profiles.forms import SearchForm, AddInterestForm


def search_interests(request):
    """
    Returns a list with all interests that contain (case insensitive) the string "query".
    """
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            query = cd["query"]
            query_type = cd["query_type"]
            interests = None
            users = None
            if query_type == "interest":
                interests = Interest.objects.filter(name__icontains=query)
            elif query_type == "user":
                users = User.objects.filter(username__icontains=query)
            return render(request, "profiles/search_results.html",
                         {"query": query, "query_type": query_type,
                          "interests": interests, "users": users})
    else:
        form = SearchForm()
    return render(request, "profiles/search_form.html", {"form": form})


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
            return HttpResponseRedirect("interest_submitted/?interest_added=" + i)
    else:
        form = AddInterestForm()
    return render(request, "profiles/addinterest.html", {"form": form})


def interest_submitted(request):
    interest = None
    if "interest_added" in request.GET and request.GET["interest_added"]:
        interest = request.GET["interest_added"]
    return render(request, "profiles/interest_submitted.html", {"interest": interest})


@login_required
def display_avatar(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, "profiles/display_avatar.html", {"profile": profile})
