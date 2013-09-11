# coding: utf-8

from django.db import models
from attach.models import ContentTypeModel


class Example(ContentTypeModel):
    """
        Exemplos serão adicionados como pedaços de códigos
        para ajudar no entendimento do usuário sobre algum item.
    """
    name = models.CharField(u'Nome', max_length=150)
    url = models.URLField(max_length=200)
    description = models.TextField(u'Descrição', blank=True)

    class Meta:
        verbose_name = 'Exemplo'
        verbose_name_plural = 'Exemplos'
        ordering = ['-added']

    def __unicode__(self):
        return self.name