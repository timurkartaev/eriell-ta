from django.db import models
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
