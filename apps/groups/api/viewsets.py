from rest_framework import viewsets

from groups.models import Group
from groups.api.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
