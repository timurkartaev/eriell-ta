from django.urls import path

from index.views import ReportListView


urlpatterns = [
    path('', ReportListView.as_view(), name='index'),
]

