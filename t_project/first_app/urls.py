from django.urls import path
from . import views

# domain.com/first_app ----> list of all the patients
urlpatterns = [
    path('', views.list_patients, name = 'list_patients')
]
