from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
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
    if 'title' in request.GET:
        title = request.GET['title']
        minsal = int(request.GET['minsal'])
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
