from django.utils.translation import ugettext_lazy as _
from django.db import models

from project.models import Project


# Create your models here.
class Talent(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Expertise(Talent):
    class Meta:
        verbose_name = _('Expertise')
        verbose_name_plural = _('Expertise')


class Skill(Talent):
    expertise = models.ManyToManyField(Expertise)

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')


class Volunteer(models.Model):
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    expertise = models.ManyToManyField(Expertise,
                                       related_name='expertise_of')
    skills = models.ManyToManyField(Skill,
                                    related_name='skills_of')
    projects = models.ManyToManyField(Project,
                                      related_name='volunteer')
    birth_date = models.DateField(_('birth date'),
                                  blank=True,
                                  null=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'


class Email(models.Model):
    email = models.EmailField(_('email'))
    volunteer = models.ForeignKey(Volunteer,
                                  on_delete=models.CASCADE,
                                  related_name='volunteer_email')

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


class Phone(models.Model):
    phone = models.CharField(_('phone'), max_length=20)
    volunteer = models.ForeignKey(Volunteer,
                                  on_delete=models.CASCADE,
                                  related_name='volunteer_phone')

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'


class Address(models.Model):
    street = models.CharField(_('street'), max_length=100)
    number = models.IntegerField(_('house number'),
                                 blank=True,
                                 null=True)
    city = models.CharField(_('city'), max_length=100)
    zip_code = models.CharField(_('zip code'), max_length=100)
    volunteer = models.ForeignKey(Volunteer,
                                  on_delete=models.CASCADE,
                                  related_name='volunteer_address')

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
