# -*- coding: utf-8 -*-

import amazonproduct
import subprocess
import os
from amazonproduct.errors import AWSError
# import cPickle
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Count
from .forms import ItemSearchForm, ItemLookUpForm
from .models import Products
from review_analysis.apps.crawler.models import Reviews
# from review_analysis.apps.classifier.views import extract_word_features

config = {
    'access_key': settings.AWS_ACCESS_KEY,
    'secret_key': settings.AWS_SECRET_KEY,
    'associate_tag': settings.AWS_ASSOCIATE_TAG,
    'locale': settings.AWS_PREFERED_LOCALE
}

api = amazonproduct.API(cfg=config)


# Create your views here.


def index(request):
    return HttpResponse("Index Page.")


def itemSearch(request):
    if request.method == 'POST':
        form = ItemSearchForm(request.POST)

        if form.is_valid():
            product_group = form.cleaned_data['productGroup']
            manufacturer = form.cleaned_data['manufacturer']
            keywords = form.cleaned_data['keywords']
            condition = form.cleaned_data['condition']

            # Search Amazon Product API
            try:
                items = api.item_search(product_group,
                                        Manufacturer=manufacturer,
                                        Keywords=keywords, Condition=condition)
            except AWSError, e:
                message = settings.AWS_ERROR_RESPONSE
                return HttpResponse(message + str(e))
            else:
                # to_unicode takes care of non-ascii characters
                inventory = []
                for item in items:
                    title = to_unicode(item.ItemAttributes.Title)
                    item_id = to_unicode(item.ASIN)
                    item_tuple = (title, item_id)
                    inventory.append(item_tuple)

            return render(request, 'products/itemResults.html',
                          {'inventory': inventory})

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
            post.reviews_url = make_url(post.asin)

            # get product title
            try:
                item_lookup = api.item_lookup(post.asin)
                for item in item_lookup.Items.Item:
                    post.product_title = item.ItemAttributes.Title
            except AWSError, e:
                message = settings.AWS_ERROR_RESPONSE
                return HttpResponse(message + str(e))
            else:
                # find crawler cfg
                os.chdir(settings.SCRAPY_APP_DIR)
                # scrapy crawl amazon_spider -a
                # start_url="https://www.amazon.com/product-reviews/B01FFQEMVQ/"
                cmd = 'scrapy crawl amazon_spider -a start_url="%s"' \
                      % post.reviews_url
                subprocess.call(cmd, shell=True)

                # TODO : save item ; B01H7XOSGO - what if they have no reviews?
                # TODO : what if item already saved
                post.save()

            # display summary from scrapped data
            reviews_summary = list(Reviews.objects.filter(asin=post.asin).
                                   values('sentiment__sentiment').
                                   annotate(total=Count('asin')).
                                   order_by('sentiment__sentiment'))
            total_reviews = Reviews.objects.filter(asin=post.asin).count()
            product_title = (Products.objects.get(asin__exact=post.asin)).\
                product_title
            asin = post.asin

            return_dict = {
                'asin': asin,
                'product_title': product_title,
                'total_reviews_extracted': total_reviews,
                'sentiment_analysis': reviews_summary
            }

        # return HttpResponse("Finished processing: " + post.reviews_url)
        return render(request, 'products/itemSummary.html',
                      {'return_dict': return_dict})

    else:
        form = ItemLookUpForm()

    return render(request, 'products/itemLookUp.html', {'form': form})


def make_url(asin):
    # https://www.amazon.com/product-reviews/B01FFQEMVQ/
    return "https://www.amazon.com/product-reviews/" + asin + "/"


def to_unicode(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj




