# coding: utf-8
import datetime
from django.views import generic

from .models import Keyword


class IndexView(generic.TemplateView):
    template_name = 'website/index.html'


class ExplainView(generic.TemplateView):
    template_name = 'website/explain.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['code'] = request.POST.get('code')
        context['keywords'] = Keyword.objects.all()
        return self.render_to_response(context)