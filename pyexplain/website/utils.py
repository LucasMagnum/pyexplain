# coding: utf-8

import json


class QuerySetEncoder(json.JSONEncoder):
    """
        QuerySetEncoder deve retornar JSON
        contendo o queryset e suas propertys
    """
    def default(self, obj):
        if hasattr(obj, 'queryset_dump'):
            return obj.queryset_dump() if callable(obj.queryset_dump) else obj.queryset_dump
        return json.JSONEncoder.default(self, obj)


queryset_dump = lambda queryset: json.dumps(queryset, cls=QuerySetEncoder)
