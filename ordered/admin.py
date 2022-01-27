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
    
class RoomOrderedLineInline(admin.StackedInline):
    model=RoomOrderedLine

class OrderedAdmin(ExportActionMixin,admin.ModelAdmin):

    list_display = ('id', 'employe', 'restaurant', 'client','total_price')
    list_filter = (
        'restaurant',
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
        RoomOrderedLineInline,
    ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(Ordered, OrderedAdmin)
