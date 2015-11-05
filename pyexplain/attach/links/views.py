# coding: utf-8

from django.views import generic

from attach.mixins import RestrictUpdateMixin, ModalContentTypeMixin

from .models import Link
from .forms import LinkForm


class LinkCreateView(ModalContentTypeMixin, generic.CreateView):
    model = Link
    form_class = LinkForm

    _target = '#links-list'


class LinkUpdateView(RestrictUpdateMixin, ModalContentTypeMixin,
                     generic.UpdateView):
    model = Link
    form_class = LinkForm

    _target = '#links-list'
