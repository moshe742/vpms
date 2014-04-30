from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

class Expertise(models.Model):
	name = models.CharField(_('name'), max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Expertise')
		verbose_name_plural = _('Expertises')


class Skill(models.Model):
	name = models.CharField(_('name'), max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('skill')
		verbose_name_plural = _('skills')


class Community(models.Model):
	name = models.CharField(_('name'), max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('community')
		verbose_name_plural = _('communities')


class Volunteer(models.Model):
	first_name = models.CharField(_('first name'), max_length=200)
	last_name = models.CharField(_('last name'), max_length=200)
	email = models.EmailField(_('email'), max_length=200)
	phone = models.CharField(_('phone'), max_length=30, blank=True)
	work_place = models.CharField(_('work place'), max_length=100, blank=True)
	home_address = models.CharField(_('home address'), max_length=300, blank=True)
	volunteer_messages = models.CharField(_('volunteer messages'), max_length=999, blank=True)
	messages_with_coordinator = models.CharField(_('messages with coordinator'), max_length=999, blank=True)
	facebook = models.URLField(max_length=200, blank=True)
	tweeter = models.URLField(max_length=200, blank=True)
	birth_date = models.DateField(blank=True, null=True)
	expertise = models.ManyToManyField(Expertise, blank=True)
	relevant_info = models.CharField(_('relevant information'), max_length=999, blank=True)
	eknight_vol = models.ManyToManyField('EKnight', related_name='volunteer')
	skill = models.ManyToManyField(Skill,related_name='skill_name', blank=True)
	community = models.ManyToManyField(Community)
	github = models.URLField(max_length=200, blank=True)
	linkedin = models.URLField(max_length=200, blank=True)
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)

	def __unicode__(self):
		return unicode(self.first_name) + unicode(self.last_name)

	class Meta:
		verbose_name = _('volunteer')
		verbose_name_plural = _('volunteers')


class Arrival(models.Model):
	user_id = models.ForeignKey(Volunteer)
	user_arrived = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.user_arrived

	class Meta:
		verbose_name = _('arrival')
		verbose_name_plural = _('arrivals')


class EKnight(models.Model):
	name = models.CharField(_('name'), max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('eknight')
		verbose_name_plural = _('eknights')
