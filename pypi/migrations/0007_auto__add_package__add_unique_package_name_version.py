# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Package'
        db.create_table(u'pypi_package', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('released_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pypi', ['Package'])

        # Adding unique constraint on 'Package', fields ['name', 'version']
        db.create_unique(u'pypi_package', ['name', 'version'])


    def backwards(self, orm):
        # Removing unique constraint on 'Package', fields ['name', 'version']
        db.delete_unique(u'pypi_package', ['name', 'version'])

        # Deleting model 'Package'
        db.delete_table(u'pypi_package')


    models = {
        u'pypi.package': {
            'Meta': {'unique_together': "(('name', 'version'),)", 'object_name': 'Package'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'released_at': ('django.db.models.fields.DateTimeField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['pypi']