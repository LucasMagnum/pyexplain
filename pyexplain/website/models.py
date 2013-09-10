# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured
from django.template.defaultfilters import truncatechars, slugify

from .templatetags.utils_tags import to_html


class SlugModel(models.Model):
    slug = models.SlugField(max_length=100, blank=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        slug_field = getattr(self, 'slug_field')

        if slug_field is None:
            raise ImproperlyConfigured(u'É necessário definir um campo para o slug')

        slug_value = getattr(self, slug_field)
        self.slug = slugify(slug_value)

        super(SlugModel, self).save(*args, **kwargs)


class Category(SlugModel):
    keyword = 'keywords'
    builtin = 'builtin'
    standard = 'standard'

    TYPE_CHOICES = (
        (keyword, u'Palavras reservadas'),
        (builtin, u'Funções embutidas'),
        (standard, u'Biblioteca padrão'),
    )
    name = models.CharField('Nome', max_length=150, unique=True)
    description = models.TextField(u'Descrição', blank=True)
    typo = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICES)

    slug_field = 'name' # qual campo irá receber o slug

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.name

    def queryset_dump(self):
        """
            Valores que devem ser retornados pelo dump de queryset
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'typo': self.typo,
            'typo_display': self.get_typo_display()
        }


class Keyword(SlugModel):
    codname = models.CharField(u'Código/Nome', max_length=150)
    description = models.TextField(u'Descrição', blank=True)
    category = models.ForeignKey(Category, related_name='keywords')

    slug_field = 'codname' # qual campo irá receber o slug

    class Meta:
        ordering = ['codname']
        unique_together = ('codname', 'category')

    def __unicode__(self):
        return self.codname

    @property
    def url(self):
        return reverse('website:keyword_detail',
            kwargs={'category_slug': self.category.slug, 'key_slug': self.slug})

    @property
    def doc_url(self):
        if self.category.typo == Category.builtin:
            return 'http://docs.python.org/2/library/functions.html#%s' % self.codname
        if self.category.typo == Category.standard:
            return 'http://docs.python.org/2/library/%s.html' % self.codname
        return

    @property
    def desc(self):
        """
            Descrição formatada.
        """
        return to_html(truncatechars(self.description, 120))

    def queryset_dump(self):
        """
            Valores que devem ser retornados pelo dump de queryset
        """
        return {
            'codname': self.codname,
            'description': self.desc,
            'url': self.url,
            'category_id': self.category_id
        }