import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    query_set = PageVisit.objects.all()
    html_template = 'home.html'
    context = {
        "page_title": "Home Page",
        "page_visits": query_set.count()
    }
    print(request.path)
    PageVisit.objects.create()
    return render(request, html_template, context=context)
