"""eriell_ta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_view

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from students.views import StudentViewSet
from marks.views import MarkViewSet, StudentAverageMark, StudentAverageMarkByGroupAndSubject
from subjects.views import SubjectViewSet
from groups.api.urls import router as group_router


router = routers.DefaultRouter()
router.register(r'users', StudentViewSet)
router.register(r'marks', MarkViewSet)
router.register(r'subjects', SubjectViewSet)


urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name='index/login.html'), name='login'),
    path('reports/students/average/', StudentAverageMark.as_view(), name='report_students_average'),
    path('reports/students/average/raw/', StudentAverageMarkByGroupAndSubject.as_view(), name='report_students_average_raw'),
    path('api/', include(router.urls)),
    path('api/', include(group_router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('index/', include('index.urls')),
    path('admin/', admin.site.urls),
]
