from django.urls import path
from . import views

urlpatterns = [
    # app의 폴더명이 첫번째 경로가 됨
    # '' 문자열 안에 들어가는 텍스트가 클라이언트 url이 됨 
    # domain.com/first_app/simple_view
    path('<topic>',views.simple_view)
]

