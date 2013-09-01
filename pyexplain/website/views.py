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
        code = request.POST.get('code')
        keywords = Keyword.objects.all()

        if code is not None:
            lines = code.split('\n')
            used_keywords = filter(
                lambda k: any(k.codname in line for line in lines),
                keywords)
            context['keywords'] = used_keywords
            context['code'] = code

        return self.render_to_response(context)


class KeywordDetail(generic.DetailView):
    model = Keyword
    context_object_name = 'keyword'
    slug_field = 'codname'
    slug_url_kwarg = 'codname'
    template_name = 'website/keyword_detail.html'