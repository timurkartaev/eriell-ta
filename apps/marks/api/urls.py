from rest_framework import routers

from marks.api.viewsets import MarkViewSet

router = routers.DefaultRouter()
router.register(r'marks', MarkViewSet)