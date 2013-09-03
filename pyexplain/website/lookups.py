# coding: utf-8

from selectable.base import ModelLookup
from selectable.registry import registry

from .models import Keyword


class KeywordLookup(ModelLookup):
    model = Keyword
    search_fields = ('codname__icontains', )

    def format_item(self, item):
        item_dict = super(KeywordLookup, self).format_item(item)
        item_dict.update({
            'url': item.url,
        })
        return item_dict

registry.register(KeywordLookup)
