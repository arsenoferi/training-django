from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.list_patient,name='list_patient'),
]