from django.shortcuts import render

from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.


def index(request):
    if request.method == "POST":
        return HttpResponseRedirect("/")
    else:
        return render(request, "index.html")
