from django.utils.translation import ugettext_lazy as _
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'))
    #project needs
    needs = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

