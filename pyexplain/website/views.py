# coding: utf-8
import json
from django.views import generic
from django import http

from .models import Keyword, Category
from .utils import queryset_dump


class IndexView(generic.TemplateView):
    template_name = 'website/index.html'


class ExplainView(generic.TemplateView):
    template_name = 'website/explain.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        code = request.POST.get('code')
        keywords = Keyword.objects.select_related('category').all()
        categorys = list(Category.objects.all())

        if code is not None:
            lines = code.split('\n')

            used_keywords = filter(
                lambda k: any(k.codname in line for line in lines),
                keywords)

            context['keywords'] = queryset_dump(used_keywords)
            context['categorys'] = categorys
            context['categorys_json'] = queryset_dump(categorys)
            context['code'] = code

        return self.render_to_response(context)


class KeywordDetail(generic.DetailView):
    model = Keyword
    context_object_name = 'keyword'
    slug_field = 'codname'
    slug_url_kwarg = 'codname'
    template_name = 'website/keyword_detail.html'


class CategoryList(generic.ListView):
    model = Category
    context_object_name = 'categorys'
    template_name = 'website/category_list.html'


class CategoryDetail(generic.DetailView):
    model = Category
    context_object_name = 'category'
    slug_field = 'name'
    slug_url_kwarg = 'name'
    template_name = 'website/category_detail.html'


def ajax_keywords(request):
    data = {
        'success': True,
    }
    return http.HttpResponse(json.dumps(data), mimetype="application/json")