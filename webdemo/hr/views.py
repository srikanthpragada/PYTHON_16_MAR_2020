from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return HttpResponse("<h1>Welcome to HR Application </h1>")


def topics(request):
    topics = ['Templates', 'Forms', 'ORM', 'REST']
    return render(request, 'topics.html',
                  {'title': 'Dango', 'topics': topics})  # request, template, context


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()  # list of dict
    return render(request, 'list_countries.html', {'countries': countries})
