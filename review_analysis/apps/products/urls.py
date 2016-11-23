# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),   
    url(r'^search/', views.search, name='search'),
    url(r'^lookup/', views.lookup, name='lookup'),
    url(r'^results/', views.results, name='results'),
]