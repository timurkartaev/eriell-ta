from rest_framework import viewsets, permissions

from marks.models import Mark
from marks.api.serializers import MarkSerializer
from marks.api.permissions import HasReportAndMarkViewPermissions


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes  = [
        permissions.IsAuthenticated,
        HasReportAndMarkViewPermissions
    ]
