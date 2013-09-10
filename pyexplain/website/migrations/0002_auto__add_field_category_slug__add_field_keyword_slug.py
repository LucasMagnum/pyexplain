# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.slug'
        db.add_column(u'website_category', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Keyword.slug'
        db.add_column(u'website_keyword', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.slug'
        db.delete_column(u'website_category', 'slug')

        # Deleting field 'Keyword.slug'
        db.delete_column(u'website_keyword', 'slug')


    models = {
        u'website.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'typo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'website.keyword': {
            'Meta': {'ordering': "['codname']", 'unique_together': "(('codname', 'category'),)", 'object_name': 'Keyword'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keywords'", 'to': u"orm['website.Category']"}),
            'codname': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['website']