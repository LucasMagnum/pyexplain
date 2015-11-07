# coding: utf-8

from django.views.generic import CreateView

from attach.mixins import RestrictUpdateMixin, ModalContentTypeMixin

from .models import Example
from .forms import ExampleForm


class ExampleMixin(object):
    model = Example
    form_class = ExampleForm
    _target = '#examples-list'


class ExampleCreateView(ExampleMixin, ModalContentTypeMixin, CreateView):
    pass


class ExampleUpdateView(ExampleMixin, RestrictUpdateMixin, ModalContentTypeMixin):
    pass
