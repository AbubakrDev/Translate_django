from django.urls import path
from .views import *

app_name = 'translate'

urlpatterns = [
    path('', home, name="home"),
    path('info/', malumot, name="malumot"),
]
