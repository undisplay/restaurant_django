# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class OrderedAdmin(admin.ModelAdmin):

    list_display = ('id', 'employe', 'date', 'service', 'table')
    list_filter = (
        'employe',
        'date',
        'id',
        'employe',
        'date',
        'service',
        'table',
    )


class DrinkOrderedLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'drink', 'quantity')
    list_filter = ('drink', 'id', 'drink', 'quantity')


class WineOrderedLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'wine', 'quantity')
    list_filter = ('wine', 'id', 'wine', 'quantity')


class MealOrderedLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'meal', 'quantity')
    list_filter = ('meal', 'id', 'meal', 'quantity')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Ordered, OrderedAdmin)
_register(models.DrinkOrderedLine, DrinkOrderedLineAdmin)
_register(models.WineOrderedLine, WineOrderedLineAdmin)
_register(models.MealOrderedLine, MealOrderedLineAdmin)
