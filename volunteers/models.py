from django.utils.translation import ugettext_lazy as _
from django.db import models

# role such as programmer, ux/ui, content
class Expertise(models.Model):
	name = models.CharField(_('name'), max_length=200)
	slug = models.CharField('slug', max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Expertise')
		verbose_name_plural = _('Expertises')


class Skill(models.Model):
	name = models.CharField(_('name'), max_length=200)
	slug = models.CharField('slug', max_length=200)
	expertise = models.ForeignKey(Expertise, related_name='expertises')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('skill')
		verbose_name_plural = _('skills')


class Community(models.Model):
	name = models.CharField(_('name'), max_length=200)
	slug = models.CharField('slug', max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('community')
		verbose_name_plural = _('communities')


class Volunteer(models.Model):
	first_name = models.CharField(_('first name'), max_length=200)
	last_name = models.CharField(_('last name'), max_length=200)
	# email = comma seperated string field, first email is most recent.
	email = models.CharField(_('email'), max_length=500)
	# phone = comma seperated string field, first phone is most recent.
	phone = models.CharField(_('phone'), max_length=100, blank=True)
	facebook = models.CharField(_('facebook'), max_length=200, blank=True)
	twitter = models.CharField(_('twitter'), max_length=200, blank=True)
	github = models.CharField(_('github'), max_length=200, blank=True)
	linkedin = models.CharField(_('linkedin'), max_length=200, blank=True)
	birth_date = models.DateField(_('birth date'), blank=True, null=True)
	expertise = models.ManyToManyField(Expertise, blank=True)
#	skill = models.ManyToManyField(Skill,related_name='skill_name', blank=True)
#	relevant_info = models.CharField(_('relevant information'), max_length=999, blank=True)
	eknights = models.ManyToManyField('EKnight', related_name='volunteers')
	community = models.ManyToManyField(Community)
	# number of arrivals before tracking arrival dates
	old_num_of_arrivals = models.IntegerField(default=0)
	created = models.DateField(_('created'), auto_now_add=True)
	updated = models.DateField(_('updated'), auto_now=True)

	def __unicode__(self):
		return unicode(self.first_name) + unicode(self.last_name)

	class Meta:
		verbose_name = _('volunteer')
		verbose_name_plural = _('volunteers')

class Admin_comment(models.Model):
	user = models.ForeignKey(Volunteer, related_name='admin_comments')
	date_time = models.DateField(_('date time'), auto_now=True)
	text = models.CharField(_('text'), max_length=800, blank=True)

	def __unicode__(self):
		return self.user_arrived

	class Meta:
		verbose_name = _('admin comment')
		verbose_name_plural = _('admin comments')

class Volunteer_work_study_place(models.Model):
	user = models.ForeignKey(Volunteer, related_name='work_study_places')
	date_time = models.DateField(_('date time'), auto_now=True)
	place = models.CharField(_('place'), max_length=800, blank=True)

	def __unicode__(self):
		return self.user_arrived

	class Meta:
		verbose_name = _('work study place')
		verbose_name_plural = _('work study places')


class Volunteer_address(models.Model):
	user = models.ForeignKey(Volunteer, related_name='addresses')
	date_time = models.DateField(_('date time'), auto_now=True)
	address = models.CharField(_('address'), max_length=800, blank=True)

	def __unicode__(self):
		return self.user_arrived

	class Meta:
		verbose_name = _('volunteer address')
		verbose_name_plural = _('volunteer addresses')


class Arrival(models.Model):
	user = models.ForeignKey(Volunteer, related_name='arrivals')
	user_arrived = models.DateField(_('user arrived'), auto_now=True)
	eknight = models.ForeignKey('EKnight', related_name='arrivals')
	#message to the coordinator
	coordinator_message = models.CharField(_('coordinator message'), max_length=800, blank=True)
	# TODO- send email to coordinator with the message

	def __unicode__(self):
		return self.user_arrived

	class Meta:
		verbose_name = _('arrival')
		verbose_name_plural = _('arrivals')

# temporary class until we merge with arnon's eknight land
class EKnight(models.Model):
	name = models.CharField(_('name'), max_length=200)
	slug = models.CharField('slug', max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('eknight')
		verbose_name_plural = _('eknights')

class Coordinator_question(models.Model):
	question = models.CharField(_('question'), max_length=200)
	date_time = models.DateField(_('date time'), auto_now=True)
	required = models.BooleanField(_('required'), default=False)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('coordinator question')
		verbose_name_plural = _('coordinator questions')


class Coordinator_question_answer(models.Model):
	answer = models.CharField(_('answer'), max_length=800)
	question = models.ForeignKey(Coordinator_question, related_name='answers')
	user = models.ForeignKey(Volunteer, related_name='answers')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('coordinator question answer')
		verbose_name_plural = _('coordinator question answers')
