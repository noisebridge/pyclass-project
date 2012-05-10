from django.shortcuts import render_to_response
from pyclass.profiles.models import Interest
from django.core.context_processors import csrf

def SearchInterests(request):
    """
    Returns a list with all interests that contain (case insensitive) the string "q".
    Validates against empty strings.
    """
    errors = []
    if "q" in request.GET:
        q = request.GET["q"]
        if not q:
            errors.append("Please enter a search term.")
        else:
            interests = Interest.objects.filter(name__icontains=q)
            return render_to_response("search_results.html",
                {"interests": interests, "query": q})
    return render_to_response("search_form.html", {"errors": errors})

def AddInterests(request):
    """
    Adds a new interest from user to database
    """
    errors = []
    if (request.POST.get('interest', -1) != -1):
        interest_list = Interest.objects.filter(name = request.POST["interest"]).count()
        if not interest_list:
            i = Interest(name = request.POST["interest"])
            i.save()
    csrf_request = {}
    csrf_request.update(csrf(request))
    return render_to_response("addinterest.html", csrf_request)
