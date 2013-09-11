# coding: utf-8

from django.views import generic

from attach.mixins import RestrictUpdateMixin, ModalContentTypeMixin

from .models import Example
from .forms import ExampleForm


class ExampleCreateView(ModalContentTypeMixin, generic.CreateView):
    model = Example
    form_class = ExampleForm

    _target = '#examples-list'


class ExampleUpdateView(RestrictUpdateMixin, ModalContentTypeMixin,
                        generic.UpdateView):
    model = Example
    form_class = ExampleForm

    _target = '#examples-list'