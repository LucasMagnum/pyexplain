# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTest(TestCase):
    def access(self, url_name, method='get'):

        method = getattr(self.client, method)
        reverse_url = reverse(url_name)

        return method(reverse_url)


class TemplateViewTest(ViewTest):
    """
        Testar se os templates utilizados estão corretos
    """
    def test_index(self):
        response = self.access('website:index')
        self.assertIn('website/index.html', response.template_name)

    def test_explain(self):
        response = self.access('website:explain')
        self.assertIn('website/explain.html', response.template_name)
