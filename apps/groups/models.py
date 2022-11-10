from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
