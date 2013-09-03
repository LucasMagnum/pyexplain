# coding: utf-8
from .forms import KeywordForm


def form_search(request):
    return {
        'form_search': KeywordForm(),
    }