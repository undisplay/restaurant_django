# vim: set fileencoding=utf-8 :
from django.contrib import admin

from import_export.admin import ExportActionMixin

from .models import *

class DrinkOrderedLineInline(admin.StackedInline):
    model=DrinkOrderedLine


class MealOrderedLineInline(admin.StackedInline):
    model=MealOrderedLine

class MenuOrderedLineInline(admin.StackedInline):
    model=MenuOrderedLine
    
class WashOrderedLineInline(admin.StackedInline):
    model=WashOrderedLine

class OrderedAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'employe', 'client','total_price')
    list_filter = (
        'employe',
        'client',
        'updated_at',
        'is_complete',
    )

    inlines=[
        MenuOrderedLineInline,
        DrinkOrderedLineInline,
        MealOrderedLineInline,
        WashOrderedLineInline,
    ]

class DrinkOrderedLineAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'ordered', 'drink', 'quantity')
    list_filter = ('ordered', 'drink', 'id', 'ordered', 'drink', 'quantity')


class WineOrderedLineAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'ordered', 'wine', 'quantity')
    list_filter = ('ordered', 'wine', 'id', 'ordered', 'wine', 'quantity')


class MealOrderedLineAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'ordered', 'meal', 'quantity')
    list_filter = ('ordered', 'meal', 'id', 'ordered', 'meal', 'quantity')


class MenuOrderedLineAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'ordered', 'menu', 'quantity')
    list_filter = ('ordered', 'menu', 'id', 'ordered', 'menu', 'quantity')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(Ordered, OrderedAdmin)
