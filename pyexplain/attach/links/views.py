# coding: utf-8

from django.views.generic import CreateView

from attach.mixins import RestrictUpdateMixin, ModalContentTypeMixin

from .models import Link
from .forms import LinkForm


class LinkMixin(object):
    model = Link
    form_class = LinkForm
    _target = '#links-list'


class LinkCreateView(LinkMixin, ModalContentTypeMixin, CreateView):
    pass


class LinkUpdateView(LinkMixin, RestrictUpdateMixin, ModalContentTypeMixin):
    pass
