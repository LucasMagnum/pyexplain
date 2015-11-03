# coding: utf-8

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class CreateModel(models.Model):
    """
        Responsável por guardar informações de quando o item
        foi criado e por quem foi criado.
    """

    added = models.DateTimeField(auto_now_add=True, editable=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class ContentTypeModel(CreateModel):
    """
        Responsável por permitir que models possam ser relacionados
        com qualquer outro model.
    """
    model = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('model', 'object_id')

    class Meta:
        abstract = True

    def delete_by(self, user):
        """
            Deleta o item se for criador ou super user.
        """
        if user.is_superuser or user is self.added_by:
            self.delete()
