# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models

class DrinkAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'sale_price','sale_price_ml', 'type')
    list_filter = ('id', 'name', 'price', 'sale_price', 'type')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Drink, DrinkAdmin)
