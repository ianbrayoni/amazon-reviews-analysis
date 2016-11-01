# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),   
    url(r'^itemSearch/', views.itemSearch, name='itemSearch'), 
    url(r'^itemLookUp/', views.itemLookUp, name='itemLookUp'), 
    url(r'^results/', views.results, name='results'),  
]