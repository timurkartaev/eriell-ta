from rest_framework import viewsets, permissions

from marks.api.permissions import HasReportAndMarkViewPermissions
from subjects.models import Subject
from subjects.api.serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        HasReportAndMarkViewPermissions
    ]
