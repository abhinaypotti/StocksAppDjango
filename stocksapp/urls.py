from django.urls import path
from .views import *

urlpatterns =[
    path('',homepageview,name='homepageview'),
    path('graph/',graphview,name='graph')
]