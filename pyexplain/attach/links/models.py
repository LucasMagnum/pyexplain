# coding: utf-8

from django.db import models
from attach.models import ContentTypeModel


LINKS_PER_OBJ = 6 # maximo de links por objetos


class Link(ContentTypeModel):
    """
        Links serão adicionados como referências externas para ajudar no
        entendimento do usuário sobre algum item.
    """
    name = models.CharField(u'Nome', max_length=150)
    url = models.URLField(max_length=200)
    description = models.TextField(u'Descrição', blank=True)

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
        return self.name