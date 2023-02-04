from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

articles = {
    'sports' : 'Sports page',
    'news' : 'News page',
    "oking's" : "Oking's page"
}

def simple_view(request, topic):
    return HttpResponse(articles[topic])