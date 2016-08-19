from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Index Page.")

def search(request):
	return HttpResponse("Search Page.")

def results(request):
	return HttpResponse("Results Page.")
