# vim: set fileencoding=utf-8 :
from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from . import models

class WashAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'type', 'wash_price')
    list_filter = ('type',)
    search_fields = ('type', 'wash_price',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Wash, WashAdmin)
