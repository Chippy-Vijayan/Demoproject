from xml.etree.ElementInclude import include
from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name="demo"),
   # path('add/',views.addition,name='addition')
]
