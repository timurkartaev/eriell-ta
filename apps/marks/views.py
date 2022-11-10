from django.db.models import Avg

from rest_framework import permissions, views
from rest_framework.response import Response

from marks.models import Mark
from marks.api.serializers import RawMarkSerializer
from marks.api.permissions import HasReportAndMarkViewPermissions


class AvgMarksByStudentView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        HasReportAndMarkViewPermissions
    ]
    
    def get(self, request, format=None):
        marks = Mark.objects.values(
            'student__first_name',
            'student__last_name',
            'group__name',
            'subject__name',
        ).annotate(avg_grade=Avg('grade'))
        return Response(marks)


class AvgMarksByGroupView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        HasReportAndMarkViewPermissions
    ]

    def get(self, request, format=None):
        raw_marks = Mark.objects.raw(
            '''
                SELECT
                    1 as id,
                    g.name as group_name,
                    s.name as subject_name,
                    AVG(m.grade) as average_grade
                FROM marks_mark as m
                LEFT JOIN subjects_subject as s ON m.subject_id = s.id
                LEFT JOIN groups_group as g ON m.group_id = g.id
                GROUP BY group_name, subject_name
            '''
        )
        serializer = RawMarkSerializer(raw_marks, many=True)
        return Response(serializer.data)
