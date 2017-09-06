from django.utils.translation import ugettext_lazy as _
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField
