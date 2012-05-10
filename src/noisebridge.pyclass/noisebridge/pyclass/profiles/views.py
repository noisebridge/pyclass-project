from django.shortcuts import render_to_response
from pyclass.profiles.models import Interest


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
