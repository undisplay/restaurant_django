# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'price', 'discount')
    list_filter = ('id', 'price', 'discount')


class MenuMealAdmin(admin.ModelAdmin):

    list_display = ('id', 'meal', 'menu', 'quantity')
    list_filter = ('meal', 'menu', 'id', 'meal', 'menu', 'quantity')


class MenuDrinkAdmin(admin.ModelAdmin):

    list_display = ('id', 'drink', 'menu', 'quantity')
    list_filter = ('drink', 'menu', 'id', 'drink', 'menu', 'quantity')


class MenuWineAdmin(admin.ModelAdmin):

    list_display = ('id', 'wine', 'menu', 'quantity')
    list_filter = ('wine', 'menu', 'id', 'wine', 'menu', 'quantity')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Menu, MenuAdmin)
_register(models.MenuMeal, MenuMealAdmin)
_register(models.MenuDrink, MenuDrinkAdmin)
_register(models.MenuWine, MenuWineAdmin)
