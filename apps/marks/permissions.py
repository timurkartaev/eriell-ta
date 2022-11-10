from rest_framework import permissions

class CheckReportAndMarkViewPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.has_perm('eriell_view_report_and_rest')