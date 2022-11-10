from rest_framework import serializers

from marks.models import Mark


class MarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mark
        fields = ('student', 'subject', 'group', 'grade')
        # depth = 1


class RawMarkSerializer(serializers.Serializer):
    group_name = serializers.CharField(max_length=255)
    subject_name = serializers.CharField(max_length=255)
    average_grade = serializers.CharField(max_length=255)