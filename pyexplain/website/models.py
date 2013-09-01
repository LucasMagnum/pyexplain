# coding: utf-8
from django.db import models


class Category(models.Model):
    keyword = 'keywords'
    builtin = 'builtin'
    standard = 'standard'

    TYPE_CHOICES = (
        (keyword, u'Palavras reservadas'),
        (builtin, u'Funções embutidas'),
        (standard, u'Biblioteca padrão'),
    )
    name = models.CharField('Nome', max_length=150)
    description = models.TextField(u'Descrição', blank=True)
    typo = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICES)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.name



class Keyword(models.Model):
    codname = models.CharField(u'Código/Nome', max_length=150)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.codname

    def get_url(self):
        typo = self.category.typo
        if typo == Category.keyword:
            return
        if typo == Category.builtin:
            return 'http://docs.python.org/2/library/functions.html#%s' % self.codname
        if typo == Category.standard:
            return 'http://docs.python.org/2/library/%s.html' % self.codname