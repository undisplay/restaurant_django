# vim: set fileencoding=utf-8 :
from django.contrib import admin

from import_export.admin import ExportActionMixin

from . import models


class EmployeAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = (
        'id',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'phone',
        'address',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'id',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'phone',
        'address',
    )
    raw_id_fields = ('groups', 'user_permissions')



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Employe, EmployeAdmin)
