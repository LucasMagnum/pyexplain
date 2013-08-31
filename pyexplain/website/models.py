# coding: utf-8

from django.db import models


class Keyword(models.Model):
    keyword = 'keywords'
    builtin = 'builtin'
    standard = 'standard'

    CATEGORY_CHOICES = (
        (keyword, u'Palavras reservadas'),
        (builtin, u'Funções embutidas'),
        (standard, u'Biblioteca padrão') 
    )

    codname = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __init__(self, *args, **kwargs):

        super(Keyword, self).__init__(self, *args, **kwargs)

    def __unicode__(self):
        return self.codname



