# vim: set fileencoding=utf-8 :
from django.contrib import admin

from .models import *

class MenuMealInline(admin.StackedInline):
    model= MenuMeal


class MenuDrinkInline(admin.StackedInline):
    model= MenuDrink


class MenuWineInline(admin.StackedInline):
    model= MenuWine

class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'discount', 'total')
    list_filter = ('id', 'name', 'discount', 'total')
    search_fields = ('name',)

    inlines = [
        MenuWineInline,
        MenuDrinkInline,
        MenuMealInline,
    ]

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


_register(Menu, MenuAdmin)
_register(MenuMeal, MenuMealAdmin)
_register(MenuDrink, MenuDrinkAdmin)
_register(MenuWine, MenuWineAdmin)
