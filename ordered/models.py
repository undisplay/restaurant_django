from django.db import models

from django.utils.translation import gettext_lazy as _

from conf.mixins import TimeStampMixin,MediaMixin

from employe.models import *
from drink.models import *
from food.models import *
from menu.models import *
from wash.models import *

class Ordered(TimeStampMixin,MediaMixin,models.Model):
    employe   = models.ForeignKey(Employe, on_delete=models.CASCADE)
    total     = models.DecimalField(_('Total'),help_text=_('Ex: 30'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    date      = models.DateField(_("Date"), auto_now_add=True)
    service   = models.CharField(_('Service'),help_text='', max_length=150, blank=False)
    table     = models.CharField(_('Table'),help_text='', max_length=150, blank=False)

    def __str__(self):
        return 'Employe:(%s) table:%s' % (self.employe,self.table)

class DrinkOrderedLine(TimeStampMixin,MediaMixin,models.Model):
    ordered  = models.ForeignKey(Ordered, on_delete=models.CASCADE)
    drink    = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Ordered:(%s) Drink:(%s)' % (self.ordered,self.drink)
    
class MealOrderedLine(TimeStampMixin,MediaMixin,models.Model):
    ordered  = models.ForeignKey(Ordered, on_delete=models.CASCADE)
    meal     = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Ordered:(%s) Meal:(%s)' % (self.ordered,self.meal)

class MenuOrderedLine(TimeStampMixin,MediaMixin,models.Model):
    ordered  = models.ForeignKey(Ordered, on_delete=models.CASCADE)
    menu     = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Ordered:(%s) Menu:(%s)' % (self.ordered,self.menu)
    
class WashOrderedLine(TimeStampMixin,MediaMixin,models.Model):
    ordered  = models.ForeignKey(Ordered, on_delete=models.CASCADE)
    wash     = models.ForeignKey(Wash, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Ordered:(%s) Wash:(%s)' % (self.ordered,self.wash)
    