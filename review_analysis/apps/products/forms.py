# -*- coding: utf-8 -*-

from django import forms
from .models import Products

PRODUCT_GROUP = (
	('', ''),
    ('Electronics', 'Electronics'),
)

MANUFACTURER = (
	('', ''),
    ('Samsung', 'Samsung'),
    ('LG', 'LG'),
    ('Sony', 'Sony'),
)

KEYWORDS = (
	('', ''),
    ('TV', 'TV'),
    ('Phone', 'Phone'),
)

CONDITION = (
	('', ''),
    ('New', 'New'),
)

class ItemSearchForm(forms.Form):
	""" Values required to search items from Amazon Product API"""
	productGroup = forms.ChoiceField(choices=PRODUCT_GROUP, required=True)
	manufacturer = forms.ChoiceField(choices=MANUFACTURER, required=True)
	keywords = forms.ChoiceField(choices=KEYWORDS, required=True)
	condition = forms.ChoiceField(choices=CONDITION, required=True)  


# class ItemLookUpForm(forms.Form):
# 	TODO : use a modelForm to store supplied items
# 	asin = forms.CharField(label='Enter ASIN', max_length=10, required=True)
# 	reviews_url = forms.CharField(widget=forms.HiddenInput(), required=False)

class ItemLookUpForm(forms.ModelForm):
	
	class Meta:
		model = Products
		fields = ('asin',)