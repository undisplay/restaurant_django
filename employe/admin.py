# vim: set fileencoding=utf-8 :
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from . import models


class RestaurantAdmin(ImportExportActionModelAdmin):

    list_display = (
        'id',
        'created_at',
        'updated_at',
        'image',
        'name',
        'phone1',
        'phone2',
        'address',
    )
    list_filter = (
        'created_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class EmployeAdmin(ImportExportActionModelAdmin):

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
        'created_at',
        'updated_at',
        'image',
        'phone',
        'address',
        'restaurant',
    )
    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active',
        'restaurant',
    )
    raw_id_fields = ('groups',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Restaurant, RestaurantAdmin)
_register(models.Employe, EmployeAdmin)
