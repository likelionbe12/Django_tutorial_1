from django.contrib import admin
from django.urls import path
#from polls import views
#from . import views
from .views import index, index1, index2

urlpatterns = [   
    path('', index),
    path('django/', index1),
    path('new/', index2),
]
