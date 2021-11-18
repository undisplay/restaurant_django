# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class WinegrowerAdmin(admin.ModelAdmin):

    list_display = ('id', 'phone', 'address')
    list_filter = ('id', 'phone', 'address')


class WineAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'winegrower',
        'creation_date',
        'price',
        'sale_price',
        'buy_date',
    )
    list_filter = (
        'winegrower',
        'creation_date',
        'buy_date',
        'id',
        'winegrower',
        'creation_date',
        'price',
        'sale_price',
        'buy_date',
    )


class DrinkAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'sale_price', 'type')
    list_filter = ('id', 'name', 'price', 'sale_price', 'type')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Winegrower, WinegrowerAdmin)
_register(models.Wine, WineAdmin)
_register(models.Drink, DrinkAdmin)
