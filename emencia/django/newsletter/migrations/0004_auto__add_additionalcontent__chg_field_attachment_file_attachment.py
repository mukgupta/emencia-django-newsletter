# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AdditionalContent'
        db.create_table(u'newsletter_additionalcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'newsletter', ['AdditionalContent'])


        # Changing field 'Attachment.file_attachment'
        db.alter_column(u'newsletter_attachment', 'file_attachment', self.gf('django.db.models.fields.files.FileField')(max_length=255))
        # Adding M2M table for field additional_objects on 'Newsletter'
        m2m_table_name = db.shorten_name(u'newsletter_newsletter_additional_objects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm[u'newsletter.newsletter'], null=False)),
            ('product', models.ForeignKey(orm[u'mineraldeco.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['newsletter_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'AdditionalContent'
        db.delete_table(u'newsletter_additionalcontent')


        # Changing field 'Attachment.file_attachment'
        db.alter_column(u'newsletter_attachment', 'file_attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100))
        # Removing M2M table for field additional_objects on 'Newsletter'
        db.delete_table(db.shorten_name(u'newsletter_newsletter_additional_objects'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mineraldeco.caliber': {
            'Meta': {'object_name': 'Caliber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'mineraldeco.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['mineraldeco.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'mineraldeco.packaging': {
            'Meta': {'object_name': 'Packaging'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'mineraldeco.product': {
            'Meta': {'ordering': "['order']", 'object_name': 'Product'},
            'caliber': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['mineraldeco.Caliber']", 'null': 'True', 'blank': 'True'}),
            'category': ('mptt.fields.TreeForeignKey', [], {'related_name': "'products'", 'to': u"orm['mineraldeco.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'packaging': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mineraldeco.Packaging']", 'through': u"orm['mineraldeco.ProductPackaging']", 'symmetrical': 'False'}),
            'photo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'sheets': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'thickness': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'mineraldeco.productpackaging': {
            'Meta': {'object_name': 'ProductPackaging'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'packaging': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mineraldeco.Packaging']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mineraldeco.Product']"})
        },
        u'newsletter.additionalcontent': {
            'Meta': {'object_name': 'AdditionalContent'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'newsletter.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'file_attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsletter.Newsletter']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'newsletter.contact': {
            'Meta': {'ordering': "('creation_date',)", 'object_name': 'Contact'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subscriber': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'tester': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'newsletter.contactmailingstatus': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'ContactMailingStatus'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsletter.Contact']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsletter.Link']", 'null': 'True', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsletter.Newsletter']"}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'newsletter.link': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'Link'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'newsletter.mailinglist': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'MailingList'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mailinglist_subscriber'", 'symmetrical': 'False', 'to': u"orm['newsletter.Contact']"}),
            'unsubscribers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'mailinglist_unsubscriber'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['newsletter.Contact']"})
        },
        u'newsletter.newsletter': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'Newsletter'},
            'additional_objects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['mineraldeco.Product']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u'<body>\\n<!-- Edit your newsletter here -->\\n</body>'"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'header_reply': ('django.db.models.fields.CharField', [], {'default': "'Mineral Deco<contact@mineral-deco.fr>'", 'max_length': '255'}),
            'header_sender': ('django.db.models.fields.CharField', [], {'default': "'Mineral Deco<contact@mineral-deco.fr>'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsletter.MailingList']"}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sending_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['newsletter.SMTPServer']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'test_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['newsletter.Contact']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'newsletter.smtpserver': {
            'Meta': {'object_name': 'SMTPServer'},
            'headers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mails_hour': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '25'}),
            'tls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'newsletter.workgroup': {
            'Meta': {'object_name': 'WorkGroup'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['newsletter.Contact']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailinglists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['newsletter.MailingList']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'newsletters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['newsletter.Newsletter']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['newsletter']