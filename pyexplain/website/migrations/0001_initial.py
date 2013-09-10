# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'website_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('typo', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'website', ['Category'])

        # Adding model 'Keyword'
        db.create_table(u'website_keyword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codname', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='keywords', to=orm['website.Category'])),
        ))
        db.send_create_signal(u'website', ['Keyword'])

        # Adding unique constraint on 'Keyword', fields ['codname', 'category']
        db.create_unique(u'website_keyword', ['codname', 'category_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Keyword', fields ['codname', 'category']
        db.delete_unique(u'website_keyword', ['codname', 'category_id'])

        # Deleting model 'Category'
        db.delete_table(u'website_category')

        # Deleting model 'Keyword'
        db.delete_table(u'website_keyword')


    models = {
        u'website.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'typo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'website.keyword': {
            'Meta': {'ordering': "['codname']", 'unique_together': "(('codname', 'category'),)", 'object_name': 'Keyword'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keywords'", 'to': u"orm['website.Category']"}),
            'codname': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['website']