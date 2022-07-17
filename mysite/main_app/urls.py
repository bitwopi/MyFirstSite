from django.urls import path
from .views import *

urlpatterns =[
    path('', MainAppHome.as_view(), name="home"),
]