# vim: set fileencoding=utf-8 :
from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin

from . import models

class DrinkAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'name','quantity_available', 'price', 'sale_price','sale_price_shot', 'type')
    list_filter = ('type',)
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Drink, DrinkAdmin)
