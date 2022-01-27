# vim: set fileencoding=utf-8 :
from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from . import models

class RoomAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'number', 'loan_price')
    list_filter = ('loan_price',)
    search_fields = ('number', 'loan_price',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Room, RoomAdmin)
