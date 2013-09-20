# coding: utf-8
from django.views import generic

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
    template_name = 'website/keyword_detail.html'

    slug_url_kwarg = 'key_slug'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        return self.model.objects.filter(category__slug=category_slug)


class CategoryList(generic.ListView):
    model = Category
    context_object_name = 'categorys'
    template_name = 'website/category_list.html'


class CategoryDetail(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'website/category_detail.html'
