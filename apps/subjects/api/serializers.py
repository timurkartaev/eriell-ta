from rest_framework import serializers

from subjects.models import Subject


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', )
