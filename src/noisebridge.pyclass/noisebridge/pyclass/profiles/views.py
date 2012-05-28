from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pyclass.profiles.models import Interest, UserProfile
from pyclass.profiles.forms import SearchForm, AddInterestForm, UserSettingsForm, UserProfileSettingsForm


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
            profile.interests.add(interest)
            profile.save()
            return HttpResponseRedirect(interest.get_absolute_url())
    else:
        form = AddInterestForm()
    return render(request, "profiles/addinterest.html", {"form": form})


def display_profile(request, user_name):
    user = None
    profile = None
    if User.objects.filter(username=user_name):
        user = User.objects.get(username=user_name)
        profile = UserProfile.objects.get(user=user)
    return render(request, "profiles/user_profile.html", {"user_name": user_name,
                                                         "user": user, "profile": profile})


@login_required
def update_settings(request):
    user = User.objects.get(username=request.user)
    profile = UserProfile.objects.get(user=user)
    if request.method == "POST":
        user_form = UserSettingsForm(request.POST, instance=user)
        profile_form = UserProfileSettingsForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(user.get_absolute_url())
    else:
        user_form = UserSettingsForm(initial={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        })
        profile_form = UserProfileSettingsForm(initial={
            "avatar": profile.avatar,
            "biography": profile.biography,
        })
    return render(request, "profiles/user_settings.html", {"user_form": user_form, "profile_form": profile_form})
