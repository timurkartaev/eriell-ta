from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from index.constants import VIEW_REPORT_AND_CRUD_PERMISSION_NAME


class ReportListView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'index/index.html'
    login_url = reverse_lazy('login')
    permission_required = VIEW_REPORT_AND_CRUD_PERMISSION_NAME

