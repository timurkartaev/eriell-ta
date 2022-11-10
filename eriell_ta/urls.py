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

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from marks.api.urls import router as marks_router
from groups.api.urls import router as groups_router
from students.api.urls import router as student_router
from subjects.api.urls import router as subject_router

# Default includes
urlpatterns = [
    path(
        'login/',
        auth_view.LoginView.as_view(template_name='index/login.html'),
        name='login'
    ),

    path('admin/', admin.site.urls),
]

# API only links 
urlpatterns += [
    path('api/', include(groups_router.urls)),
    path('api/', include(marks_router.urls)),
    path('api/', include(student_router.urls)),
    path('api/', include(subject_router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

# Apps includes
urlpatterns += [
    path('', include('index.urls')),
    path('', include('marks.urls')),
]
