from rest_framework import routers

from groups.api.viewsets import GroupViewSet


router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)