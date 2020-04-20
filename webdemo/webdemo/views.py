from django.http import HttpResponse


def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome To Django</h1>")  # Response


def greet(request):
    # Create message based on current time
    pass
