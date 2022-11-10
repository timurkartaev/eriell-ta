from rest_framework import permissions

from index.utils import hasPermViewReport

class HasReportAndMarkViewPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return hasPermViewReport(request.user)