# coding: utf-8

import json

from django.contrib.contenttypes.models import ContentType
from django.views import generic
from django.http import HttpResponse

from attach.decorators import LoginRequiredMixin, RestrictUpdateMixin

from .models import Link
from .forms import LinkForm


class LinkCreateView(LoginRequiredMixin, generic.CreateView):
    model = Link
    form_class = LinkForm
    template_name = 'links/modal_form.html'

    @property
    def valid_message(self):
        return u'Link criado com sucesso.'

    def get_content_object(self):
        obj_id = self.kwargs.pop('obj_id')
        content = ContentType.objects.get(**self.kwargs)
        return content.get_object_for_this_type(pk=obj_id)

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.instance.content_object = self.get_content_object()
        form.instance.save()

        data = {
            'message': self.valid_message,
            'status': 200,
            'success': True,
            'target': '#links-list', # selector HTML que deve ser atualizado.
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


class LinkUpdateView(RestrictUpdateMixin, generic.UpdateView):
    model = Link
    form_class = LinkForm
    template_name = 'links/modal_form.html'

    @property
    def valid_message(self):
        return u'Link atualizado com sucesso.'

    def form_valid(self, form):
        form.instance.save()
        data = {
            'message': self.valid_message,
            'status': 200,
            'success': True,
            'target': '#links-list', # selector HTML que deve ser atualizado.
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
