# coding: utf-8
from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse

from selenium import webdriver


class AccessViewTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_url(self, url_name):
        return self.live_server_url + reverse('website:' + url_name)

    def test_tour_indexpage(self):
        """
            Testar se aparece a opção para o tour inicial
        """
        self.browser.get(self.get_url('index'))
        tour_link = self.browser.find_element_by_class_name('show_tour')
        self.assertTrue(tour_link.is_displayed())

    def test_send_code(self):
        self.browser.get(self.get_url('index'))

        # adicionar o código no textarea
        code_area = self.browser.find_element_by_name('code')
        code_area.send_keys('from datetime import datetime')

        # enviar o código
        submit = self.browser.find_element_by_css_selector('[type=submit]')
        submit.click()

        self.assertEqual(self.get_url('explain'), self.browser.current_url)

    def test_send_without_code(self):
        self.browser.get(self.get_url('index'))

        # enviar o código, deve dar erro
        submit = self.browser.find_element_by_css_selector('[type=submit]')
        submit.click()

        # o form deve apresentar erro
        element = self.browser.find_element_by_class_name('has-error')
        self.assertEqual('form', element.tag_name)

        # e o usuario deve permanecer na mesma página
        self.assertEqual(self.get_url('index'), self.browser.current_url)
