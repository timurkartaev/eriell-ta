from rest_framework import routers

from students.api.viewsets import StudentViewSet

router = routers.DefaultRouter()


router.register(r'students', StudentViewSet)
