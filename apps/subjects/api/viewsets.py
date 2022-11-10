from rest_framework import viewsets

from subjects.models import Subject
from subjects.api.serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
