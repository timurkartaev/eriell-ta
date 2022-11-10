from rest_framework import viewsets, permissions

from marks.api.permissions import HasReportAndMarkViewPermissions
from groups.models import Group
from groups.api.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        HasReportAndMarkViewPermissions
    ]
