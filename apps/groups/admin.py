from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group, GroupAdmin)
