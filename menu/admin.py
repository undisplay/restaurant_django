# vim: set fileencoding=utf-8 :
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

class MenuMealInline(admin.StackedInline):
    model= MenuMeal


class MenuDrinkInline(admin.StackedInline):
    model= MenuDrink


class MenuAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'name', 'discount',)
    list_filter = ('id', 'name', 'discount',)
    search_fields = ('name',)

    inlines = [
        MenuDrinkInline,
        MenuMealInline,
    ]

class MenuMealAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'meal', 'menu', 'quantity')
    list_filter = ('meal', 'menu', 'id', 'meal', 'menu', 'quantity')


class MenuDrinkAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'drink', 'menu', 'quantity')
    list_filter = ('drink', 'menu', 'id', 'drink', 'menu', 'quantity')


class MenuWineAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'wine', 'menu', 'quantity')
    list_filter = ('wine', 'menu', 'id', 'wine', 'menu', 'quantity')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


# _register(Menu, MenuAdmin)
# _register(MenuMeal, MenuMealAdmin)
# _register(MenuDrink, MenuDrinkAdmin)
