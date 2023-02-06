from django.urls import path
from . import views

urlpatterns = [
    path('',views.example_view),
    path('variable/',views.variable_view)
]