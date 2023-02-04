from django.urls import path
from . import views # .은 현재 디렉토리 현재 디렉토리에 views를 import해라

urlpatterns = [
    path('', views.index, name = 'index') # /my_apps --> Project urls.py
]

