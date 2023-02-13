from django.urls import path
from . import views

# 앱 폴더랑 이름 같아야 함
app_name = 'cars'

urlpatterns = [
    path('list/', views.list, name = 'list'),
    path('add/', views.add, name = 'add'),
    path('delete/', views.delete, name = 'delete'),
]
