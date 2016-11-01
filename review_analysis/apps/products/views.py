# -*- coding: utf-8 -*-

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

			# to_unicode takes care of non-ascii characters
			inventory=[]
			for item in items:
				title = to_unicode(item.ItemAttributes.Title)
				item_id = to_unicode(item.ASIN)
				item_tuple = (title,item_id)
				inventory.append(item_tuple)

			return render(request, 'products/itemResults.html',{'inventory': inventory})

	else:
		form = ItemSearchForm()

	return render(request, 'products/itemSearch.html', {'form': form})



def results(request):
	return HttpResponse("Results Page.")


def itemLookUp(request):
	if request.method == 'POST':
		form = ItemLookUpForm(request.POST)		

		if form.is_valid():
			post = form.save(commit=False)
			post.asin = form.cleaned_data['asin']
			post.reviews_url = makeUrl(post.asin)

			# get product title
			itemLookup = api.item_lookup(post.asin)
			for item in itemLookup.Items.Item:
				post.product_title = item.ItemAttributes.Title			

			# find crawler cfg
			# reference in settings
			os.chdir("/home/brayoni/CodeHub/Reviews/amazon_crawler")
			# scrapy crawl amazon_spider -a start_url="https://www.amazon.com/product-reviews/B01FFQEMVQ/"
			cmd = 'scrapy crawl amazon_spider -a start_url="%s"' % post.reviews_url
			subprocess.call(cmd, shell=True)
			
			# save item ; B01H7XOSGO - what if they have no reviews?
			# what if item already saved
			post.save()
			
		return HttpResponse("Finished processing: " + post.reviews_url)

	else:
		form = ItemLookUpForm()

	return render(request, 'products/itemLookUp.html', {'form': form})

def makeUrl(asin):
	# https://www.amazon.com/product-reviews/B01FFQEMVQ/
	return "https://www.amazon.com/product-reviews/" + asin + "/"

def to_unicode(obj, encoding='utf-8'):
	if isinstance(obj, basestring):
		if not isinstance(obj,unicode):
			obj = unicode(obj,encoding)
	return obj

