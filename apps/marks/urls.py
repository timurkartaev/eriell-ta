from django.urls import path


from marks.views import AvgMarksByStudentView, AvgMarksByGroupView

urlpatterns = [
    path(
        'reports/marks-by-students/',
        AvgMarksByStudentView.as_view(),
        name='marks_by_students_view'
    ),

    path(
        'reports/marks-by-groups/',
        AvgMarksByGroupView.as_view(),
        name='marks_by_groups_view'
    )
]
