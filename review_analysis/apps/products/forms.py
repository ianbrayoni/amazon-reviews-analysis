# -*- coding: utf-8 -*-

from django import forms
from .models import Product

PRODUCT_GROUP = (
    # ('', ''),
    ('Electronics', 'Electronics'),
)

MANUFACTURER = (
    ('', ''),
    ('Samsung', 'Samsung'),
    ('LG', 'LG'),
    ('Sony', 'Sony'),
    ('Apple', 'Apple'),
)

KEYWORDS = (
    ('', ''),
    ('TV', 'TV'),
    ('Phone', 'Phone'),
)

CONDITION = (
    ('', ''),
    ('New', 'New'),
    ('Refurbished', 'Refurbished'),
)


class ItemSearchForm(forms.Form):
    """ Values required to search items from Amazon Product API"""
    productGroup = forms.ChoiceField(choices=PRODUCT_GROUP, required=True)
    manufacturer = forms.ChoiceField(choices=MANUFACTURER, required=True)
    keywords = forms.ChoiceField(choices=KEYWORDS, required=True)
    condition = forms.ChoiceField(choices=CONDITION, required=True)


class ItemLookUpForm(forms.ModelForm):
    """
    LookUp: asin, product_title, reviews_url
    """
    class Meta:
        model = Product
        fields = ('asin',)
