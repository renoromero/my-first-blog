from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

def cll(request):
    return render(request, "colling.html")
    