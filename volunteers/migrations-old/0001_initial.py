# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Expertise'
        db.create_table(u'volunteers_expertise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'volunteers', ['Expertise'])

        # Adding model 'Skill'
        db.create_table(u'volunteers_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('expertise', self.gf('django.db.models.fields.related.ForeignKey')(related_name='expertises', to=orm['volunteers.Expertise'])),
        ))
        db.send_create_signal(u'volunteers', ['Skill'])

        # Adding model 'Community'
        db.create_table(u'volunteers_community', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'volunteers', ['Community'])

        # Adding model 'Volunteer'
        db.create_table(u'volunteers_volunteer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('work_place', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('home_address', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('volunteer_messages', self.gf('django.db.models.fields.CharField')(max_length=999, blank=True)),
            ('messages_with_coordinator', self.gf('django.db.models.fields.CharField')(max_length=999, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('relevant_info', self.gf('django.db.models.fields.CharField')(max_length=999, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'volunteers', ['Volunteer'])

        # Adding M2M table for field expertise on 'Volunteer'
        m2m_table_name = db.shorten_name(u'volunteers_volunteer_expertise')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteer', models.ForeignKey(orm[u'volunteers.volunteer'], null=False)),
            ('expertise', models.ForeignKey(orm[u'volunteers.expertise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['volunteer_id', 'expertise_id'])

        # Adding M2M table for field eknights on 'Volunteer'
        m2m_table_name = db.shorten_name(u'volunteers_volunteer_eknights')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteer', models.ForeignKey(orm[u'volunteers.volunteer'], null=False)),
            ('eknight', models.ForeignKey(orm[u'volunteers.eknight'], null=False))
        ))
        db.create_unique(m2m_table_name, ['volunteer_id', 'eknight_id'])

        # Adding M2M table for field skill on 'Volunteer'
        m2m_table_name = db.shorten_name(u'volunteers_volunteer_skill')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteer', models.ForeignKey(orm[u'volunteers.volunteer'], null=False)),
            ('skill', models.ForeignKey(orm[u'volunteers.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['volunteer_id', 'skill_id'])

        # Adding M2M table for field community on 'Volunteer'
        m2m_table_name = db.shorten_name(u'volunteers_volunteer_community')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteer', models.ForeignKey(orm[u'volunteers.volunteer'], null=False)),
            ('community', models.ForeignKey(orm[u'volunteers.community'], null=False))
        ))
        db.create_unique(m2m_table_name, ['volunteer_id', 'community_id'])

        # Adding model 'Admin_comment'
        db.create_table(u'volunteers_admin_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='admin_comments', to=orm['volunteers.Volunteer'])),
            ('date_time', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=800, blank=True)),
        ))
        db.send_create_signal(u'volunteers', ['Admin_comment'])

        # Adding model 'Volunteer_work_study_place'
        db.create_table(u'volunteers_volunteer_work_study_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_study_places', to=orm['volunteers.Volunteer'])),
            ('date_time', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=800, blank=True)),
        ))
        db.send_create_signal(u'volunteers', ['Volunteer_work_study_place'])

        # Adding model 'Arrival'
        db.create_table(u'volunteers_arrival', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='arrivals', to=orm['volunteers.Volunteer'])),
            ('user_arrived', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('eknight', self.gf('django.db.models.fields.related.ForeignKey')(related_name='arrivals', to=orm['volunteers.EKnight'])),
            ('coordinator_message', self.gf('django.db.models.fields.CharField')(max_length=800, blank=True)),
        ))
        db.send_create_signal(u'volunteers', ['Arrival'])

        # Adding model 'EKnight'
        db.create_table(u'volunteers_eknight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'volunteers', ['EKnight'])


    def backwards(self, orm):
        # Deleting model 'Expertise'
        db.delete_table(u'volunteers_expertise')

        # Deleting model 'Skill'
        db.delete_table(u'volunteers_skill')

        # Deleting model 'Community'
        db.delete_table(u'volunteers_community')

        # Deleting model 'Volunteer'
        db.delete_table(u'volunteers_volunteer')

        # Removing M2M table for field expertise on 'Volunteer'
        db.delete_table(db.shorten_name(u'volunteers_volunteer_expertise'))

        # Removing M2M table for field eknights on 'Volunteer'
        db.delete_table(db.shorten_name(u'volunteers_volunteer_eknights'))

        # Removing M2M table for field skill on 'Volunteer'
        db.delete_table(db.shorten_name(u'volunteers_volunteer_skill'))

        # Removing M2M table for field community on 'Volunteer'
        db.delete_table(db.shorten_name(u'volunteers_volunteer_community'))

        # Deleting model 'Admin_comment'
        db.delete_table(u'volunteers_admin_comment')

        # Deleting model 'Volunteer_work_study_place'
        db.delete_table(u'volunteers_volunteer_work_study_place')

        # Deleting model 'Arrival'
        db.delete_table(u'volunteers_arrival')

        # Deleting model 'EKnight'
        db.delete_table(u'volunteers_eknight')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'volunteers.eknight': {
            'Meta': {'object_name': 'EKnight'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'volunteers.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'community': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['volunteers.Community']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'eknights': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'volunteers'", 'symmetrical': 'False', 'to': u"orm['volunteers.EKnight']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'expertise': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['volunteers.Expertise']", 'symmetrical': 'False', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'home_address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'messages_with_coordinator': ('django.db.models.fields.CharField', [], {'max_length': '999', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'relevant_info': ('django.db.models.fields.CharField', [], {'max_length': '999', 'blank': 'True'}),
            'skill': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'skill_name'", 'blank': 'True', 'to': u"orm['volunteers.Skill']"}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'volunteer_messages': ('django.db.models.fields.CharField', [], {'max_length': '999', 'blank': 'True'}),
            'work_place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
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