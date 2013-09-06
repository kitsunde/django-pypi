# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Version', fields ['package', 'version']
        db.delete_unique(u'pypi_version', ['package_id', 'version'])

        # Removing unique constraint on 'Release', fields ['version', 'upload_time']
        db.delete_unique(u'pypi_release', ['version_id', 'upload_time'])

        # Deleting model 'Package'
        db.delete_table(u'pypi_package')

        # Deleting model 'Release'
        db.delete_table(u'pypi_release')

        # Deleting model 'Version'
        db.delete_table(u'pypi_version')


    def backwards(self, orm):
        # Adding model 'Package'
        db.create_table(u'pypi_package', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
        ))
        db.send_create_signal(u'pypi', ['Package'])

        # Adding model 'Release'
        db.create_table(u'pypi_release', (
            ('comment_text', self.gf('django.db.models.fields.TextField')()),
            ('python_version', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('md5_digest', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('downloads', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('packagetype', self.gf('django.db.models.fields.CharField')(max_length=13)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('has_sig', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('upload_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('version', self.gf('django.db.models.fields.related.ForeignKey')(related_name='releases', to=orm['pypi.Version'])),
        ))
        db.send_create_signal(u'pypi', ['Release'])

        # Adding unique constraint on 'Release', fields ['version', 'upload_time']
        db.create_unique(u'pypi_release', ['version_id', 'upload_time'])

        # Adding model 'Version'
        db.create_table(u'pypi_version', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(related_name='versions', to=orm['pypi.Package'])),
        ))
        db.send_create_signal(u'pypi', ['Version'])

        # Adding unique constraint on 'Version', fields ['package', 'version']
        db.create_unique(u'pypi_version', ['package_id', 'version'])


    models = {
        
    }

    complete_apps = ['pypi']