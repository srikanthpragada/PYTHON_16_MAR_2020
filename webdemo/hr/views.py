from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
import requests
from .forms import DiscountForm
from datetime import datetime


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


def delete_job(request):
    id = request.GET['id']
    con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
    cur = con.cursor()
    # cur.execute("insert into jobs (title,minsalary) values(?,?)", (title,minsal))
    con.commit()
    con.close()
    return redirect("/hr/jobs")


def add_job(request):
    # if data is passed then process it
    if 'title' in request.POST:
        title = request.POST['title']
        minsal = int(request.POST['minsal'])
        con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
        cur = con.cursor()
        cur.execute("insert into jobs (title,minsalary) values(?,?)", (title, minsal))
        con.commit()
        con.close()
        return redirect("/hr/jobs")
    else:
        return render(request, 'add_job.html')


def list_jobs(request):
    con = sqlite3.connect(r"c:\classroom\mar16\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs")
    return render(request, 'list_jobs.html', {'jobs': cur.fetchall()})


def discount(request):
    if request.method == "GET":
        f = DiscountForm()
        return render(request, 'discount.html', {'form': f})
    else:
        f = DiscountForm(request.POST)  # Bind client's data
        if f.is_valid():
            amount = f.cleaned_data['amount']
            rate = f.cleaned_data['rate']
            discount = amount * rate / 100
            return render(request, 'discount.html', {'form': f, 'discount': discount})
        else:
            return render(request, 'discount.html', {'form': f})


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def get_datetime(request):
    return HttpResponse(str(datetime.now()))
