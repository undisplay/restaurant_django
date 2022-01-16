# vim: set fileencoding=utf-8 :
from django.contrib import admin

from .models import *

class DrinkOrderedLineInline(admin.StackedInline):
    model=DrinkOrderedLine


class MealOrderedLineInline(admin.StackedInline):
    model=MealOrderedLine

class MenuOrderedLineInline(admin.StackedInline):
    model=MenuOrderedLine
    
class WashOrderedLineInline(admin.StackedInline):
    model=WashOrderedLine

class OrderedAdmin(admin.ModelAdmin):

    list_display = ('id', 'employe', 'client')
    list_filter = (
        'employe',
        'client',
    )

    inlines=[
        MenuOrderedLineInline,
        DrinkOrderedLineInline,
        MealOrderedLineInline,
        WashOrderedLineInline,
    ]

class DrinkOrderedLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'ordered', 'drink', 'quantity')
    list_filter = ('ordered', 'drink', 'id', 'ordered', 'drink', 'quantity')


class WineOrderedLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'ordered', 'wine', 'quantity')
    list_filter = ('ordered', 'wine', 'id', 'ordered', 'wine', 'quantity')


class MealOrderedLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'ordered', 'meal', 'quantity')
    list_filter = ('ordered', 'meal', 'id', 'ordered', 'meal', 'quantity')


class MenuOrderedLineAdmin(admin.ModelAdmin):

    list_display = ('id', 'ordered', 'menu', 'quantity')
    list_filter = ('ordered', 'menu', 'id', 'ordered', 'menu', 'quantity')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(Ordered, OrderedAdmin)
