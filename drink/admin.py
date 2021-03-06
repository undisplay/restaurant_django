# vim: set fileencoding=utf-8 :
from django.contrib import admin

from import_export.admin import ExportActionMixin

from . import models

class DrinkAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'name','quantity_available', 'price', 'sale_price','sale_price_ml', 'type')
    list_filter = ('type',)
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Drink, DrinkAdmin)
