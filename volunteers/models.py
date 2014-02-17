from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

class Project(models.Model):
	name = models.CharField(_('name'), max_length=200)

	def __unicode__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Volunteer(models.Model):
	name = models.CharField(_('name'), max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=30)
	project = models.ForeignKey(Project, blank=True, null=True)
	skill = models.ManyToManyField(Skill,)
	created = models.DateField(auto_now_add=True)
	arrived = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.name
