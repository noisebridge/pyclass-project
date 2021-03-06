from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from pyclass.profiles.models import Interest
from pyclass.profiles.forms import SearchForm, AddInterestForm, UserSettingsForm, UserProfileSettingsForm


def search_interests(request):
    """
    Returns a list with all interests that contain (case insensitive) the string "query".
    """
    if "query" and "query_type" in request.GET:
        form = SearchForm(request.GET)
        if not form.is_valid():
            messages.error(request, "Form contains errors.")
        else:
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
    Adds interests to the user's profile.
    If an interest doesn't exist, adds it to the database first.
    """
    if request.method == "POST":
        form = AddInterestForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Form contains errors.")
        else:
            profile = request.user.userprofile
            interests = form.cleaned_data["interests"]
            for i in interests:
                interest_list = Interest.objects.filter(name=i).count()
                if not interest_list:
                    interest = Interest(name=i)
                    interest.save()
                else:
                    interest = Interest.objects.get(name=i)
                profile.interests.add(interest)
            profile.save()
            if len(interests) > 1:
                messages.success(request, "Interests added.")
                return redirect(request.user)
            else:
                messages.success(request, "Interest added.")
                return redirect(interest)
    else:
        form = AddInterestForm()
    return render(request, "profiles/addinterest.html", {"form": form})


def display_profile(request, user_name):
    requested_user = None
    profile = None
    if User.objects.filter(username=user_name):
        requested_user = User.objects.get(username=user_name)
        profile = requested_user.userprofile
    return render(request, "profiles/user_profile.html", {"user_name": user_name,
                                                         "requested_user": requested_user,
                                                         "profile": profile})


@login_required
def update_settings(request):
    user = request.user
    profile = user.userprofile
    if request.method == "POST":
        user_form = UserSettingsForm(request.POST, instance=user)
        profile_form = UserProfileSettingsForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile details updated.")
            return redirect(user)
        else:
            messages.error(request, "Form contains errors.")
    else:
        # Done as two forms because we're using generic model forms
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


@login_required
def reset_avatar(request):
    if request.method == "POST":
        user = request.user
        user.userprofile.reset_avatar()
        messages.success(request, "Avatar reset.")
        return redirect(user)
    return render(request, "confirm_action.html",
                 {"title": "Reset Avatar",
                 "message": "Are you sure you want to reset your avatar to the default?"
    })
