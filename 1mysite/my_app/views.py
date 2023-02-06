from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 여기가 페이지에서 보여지는 곳이네요
def index(request):
    return HttpResponse("헬로다 헬로 자식들아")