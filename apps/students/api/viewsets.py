from rest_framework import viewsets, permissions


from marks.api.permissions import HasReportAndMarkViewPermissions

from students.models import Student
from students.api.serializers import StudentSerializer



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('first_name')
    serializer_class = StudentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        HasReportAndMarkViewPermissions
    ]
