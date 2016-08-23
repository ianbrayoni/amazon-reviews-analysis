from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemSearchForm, ItemLookUpForm
import amazonproduct
import subprocess
import os

config = {
    'access_key': 'AKIAIISQG525FSEYBPZA',
    'secret_key': 'BNHIdzWT02iMGaRcaWG3N6Tz1XNuBrDFg+NLLhcd',
    'associate_tag': 'revanalytics2-20',
    'locale': 'us'
}

api = amazonproduct.API(cfg=config)

# Create your views here.

def index(request):
	return HttpResponse("Index Page.")

def itemSearch(request):
	if request.method == 'POST':
		form = ItemSearchForm(request.POST)		

		if form.is_valid():
			productGroup = form.cleaned_data['productGroup']
			manufacturer = form.cleaned_data['manufacturer']
			keywords = form.cleaned_data['keywords']
			condition = form.cleaned_data['condition']

			# Search Amazon Product API
			items = api.item_search(productGroup,Manufacturer=manufacturer,Keywords=keywords,Condition=condition)

			return render(request, 'products/itemResults.html',{'items': items})

	else:
		form = ItemSearchForm()

	return render(request, 'products/itemSearch.html', {'form': form})



def results(request):
	return HttpResponse("Results Page.")


def itemLookUp(request):
	if request.method == 'POST':
		form = ItemLookUpForm(request.POST)		

		if form.is_valid():
			asin = form.cleaned_data['asin']
			form.cleaned_data['reviews_url'] = makeUrl(asin)
			url = form.cleaned_data['reviews_url'] 
			# find crawler cfg
			os.chdir("/home/brayoni/CodeHub/Reviews/amazon_crawler")
			# scrapy crawl amazon_spider -a start_url="https://www.amazon.com/product-reviews/B01FFQEMVQ/"
			cmd = 'scrapy crawl amazon_spider -a start_url="%s"' % url
			subprocess.call(cmd, shell=True)
			
		return HttpResponse("Finished processing: " url)

	else:
		form = ItemLookUpForm()

	return render(request, 'products/itemLookUp.html', {'form': form})

def makeUrl(asin):
	# https://www.amazon.com/product-reviews/B01FFQEMVQ/
	return "https://www.amazon.com/product-reviews/" + asin + "/"