from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    name = models.CharField(_('Subject'), max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
