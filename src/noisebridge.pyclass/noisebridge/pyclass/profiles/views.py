from django.shortcuts import render_to_response
from django.http import HttpResponse
from pyclass.profiles.models import Interest


def search_form(request):
    return render_to_response("search_form.html")


def search(request):
    if "q" in request.GET and request.GET['q']:
        q = request.GET["q"]
        interests = Interest.objects.filter(name__icontains=q)
        return render_to_response("search_results.html",
            {"interests": interests, "query": q})
    else:
        return HttpResponse("Please submit a search term.")
