from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

articles = {
    'sports' : 'Sports page',
    'news' : 'News page',
    "oking's" : "Oking's page"
}

def simple_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404()

def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f'{num1} + {num2} = {add_result}'
    return HttpResponse(result)

def num_page_view(request,num_page):
    try:
        topic_list = list(articles.keys())
        topic = topic_list[num_page]
        
        return HttpResponseRedirect(reverse('topic-page', args = [topic]))
    except:
        raise Http404()
    

