from index.constants import VIEW_REPORT_AND_CRUD_PERMISSION_NAME


def hasPermViewReport(user):
    return user.has_perm(VIEW_REPORT_AND_CRUD_PERMISSION_NAME)