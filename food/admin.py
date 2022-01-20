# vim: set fileencoding=utf-8 :
from django.contrib import admin

from import_export.admin import ExportActionMixin

from . import models


class MealAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'name','quantity_available', 'sale_price', 'type')
    list_filter = ('type',)
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Meal, MealAdmin)
