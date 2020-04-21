from datetime import datetime

from django.http import HttpResponse


def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome To Django</h1>")  # Response


def greet(request):
    # Create message based on current time
    hour = datetime.now().hour
    if hour < 12:
        msg = "Good Morning!"
    elif hour < 17:
        msg = "Good Afternoon!"
    else:
        msg = "Good Evening!"

    return HttpResponse(f"<h1 style='color:red'>{msg}</h1>")  # Response

