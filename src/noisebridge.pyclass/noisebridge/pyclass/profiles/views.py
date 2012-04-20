from django.shortcuts import render_to_response


def index(response):
    return render_to_response("index.html")
