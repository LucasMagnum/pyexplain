# coding: utf-8
from django import forms

from selectable.forms import AutoCompleteSelectWidget

from .lookups import KeywordLookup


class KeywordForm(forms.Form):
    keyword = forms.CharField(
        widget=AutoCompleteSelectWidget(
            lookup_class=KeywordLookup,
            attrs={'class': 'form-control col-xs-12', 'placeholder': 'Buscar'}
        ))