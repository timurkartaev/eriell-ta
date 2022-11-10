from rest_framework import routers

from subjects.api.viewsets import SubjectViewSet


router = routers.DefaultRouter()

router.register(r'subjects', SubjectViewSet)
