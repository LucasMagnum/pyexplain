# coding: utf-8

from django.db import models
from attach.models import ContentTypeModel


class Example(ContentTypeModel):
    """
        Exemplos serão adicionados como pedaços de códigos
        para ajudar no entendimento do usuário sobre algum item.
    """
    name = models.CharField(u'Nome', max_length=150, blank=True)
    code = models.TextField(u'Código')

    class Meta:
        verbose_name = 'Exemplo'
        verbose_name_plural = 'Exemplos'
        ordering = ['-added']

    def __unicode__(self):
        return self.name