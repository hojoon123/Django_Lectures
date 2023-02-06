from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

def simple_view(request):
    return render(request,'second_app/example.html') #.html