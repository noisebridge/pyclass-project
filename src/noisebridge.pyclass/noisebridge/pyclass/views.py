from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def users(request, user_name):
    return render(request, "profile.html", {"user_name":user_name})
