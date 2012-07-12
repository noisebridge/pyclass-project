from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from pyclass.profiles.models import Interest


def index(request):
    return render(request, "index.html")

def search(request):
    '''
        Used to process search form. If user does not submit a valid for they
        are shown a new search form
    '''
    search_term = request.GET['s']
    if search_term:
        interests = Interest.objects.filter(name__icontains=search_term)
        users = User.objects.filter(username__icontains=search_term)
        return render(request, "search_results.html", {"search_term": search_term,
            "users": users, "interests" : interests})

    messages.error(request, "You didn't ask for anything")
    return render(request, "search_results.html")

