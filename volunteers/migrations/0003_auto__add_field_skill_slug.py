# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Skill.slug'
        db.add_column(u'volunteers_skill', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Skill.slug'
        db.delete_column(u'volunteers_skill', 'slug')


    models = {
        u'volunteers.admin_comment': {
            'Meta': {'object_name': 'Admin_comment'},
            'date_time': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'admin_comments'", 'to': u"orm['volunteers.Volunteer']"})
        },
        u'volunteers.arrival': {
            'Meta': {'object_name': 'Arrival'},
            'coordinator_message': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'eknight': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'arrivals'", 'to': u"orm['volunteers.EKnight']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'arrivals'", 'to': u"orm['volunteers.Volunteer']"}),
            'user_arrived': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'volunteers.community': {
            'Meta': {'object_name': 'Community'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'volunteers.coordinator_question': {
            'Meta': {'object_name': 'Coordinator_question'},
            'date_time': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'volunteers.coordinator_question_answer': {
            'Meta': {'object_name': 'Coordinator_question_answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['volunteers.Coordinator_question']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['volunteers.Volunteer']"})
        },
        u'volunteers.eknight': {
            'Meta': {'object_name': 'EKnight'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'volunteers.expertise': {
            'Meta': {'object_name': 'Expertise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'volunteers.skill': {
            'Meta': {'object_name': 'Skill'},
            'expertise': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'expertises'", 'to': u"orm['volunteers.Expertise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'volunteers.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'community': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['volunteers.Community']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'eknights': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'volunteers'", 'symmetrical': 'False', 'to': u"orm['volunteers.EKnight']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'expertise': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['volunteers.Expertise']", 'symmetrical': 'False', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'relevant_info': ('django.db.models.fields.CharField', [], {'max_length': '999', 'blank': 'True'}),
            'skill': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'skill_name'", 'blank': 'True', 'to': u"orm['volunteers.Skill']"}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'volunteers.volunteer_address': {
            'Meta': {'object_name': 'Volunteer_address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'date_time': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': u"orm['volunteers.Volunteer']"})
        },
        u'volunteers.volunteer_work_study_place': {
            'Meta': {'object_name': 'Volunteer_work_study_place'},
            'date_time': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_study_places'", 'to': u"orm['volunteers.Volunteer']"})
        }
    }

    complete_apps = ['volunteers']