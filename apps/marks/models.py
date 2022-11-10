from django.db import models
from django.utils.translation import gettext_lazy as _

from students.models import Student
from groups.models import Group
from subjects.models import Subject


class Mark(models.Model):
    GRADE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=50)

    def __str__(self):
        return f'{self.student}-{self.subject}-{self.group}-{self.grade}'

    class Meta:
        verbose_name = _('Mark')
        verbose_name_plural = _('Marks')
        permissions = [
            ('eriell_view_report_and_rest', 'Can view report and CRUD Mark')
        ]
