from django.db import models

from django.utils.translation import gettext_lazy as _

from employe.models import *
from drink.models import *
from food.models import *

class Ordered(models.Model):
    employe   = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date      = models.DateField(_("Date"), auto_now_add=True)
    service   = models.CharField(_('Service'),help_text='', max_length=150, blank=False)
    table     = models.CharField(_('Table'),help_text='', max_length=150, blank=False)

class DrinkOrderedLine(models.Model):
    drink    = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

class WineOrderedLine(models.Model):
    wine     = models.ForeignKey(Wine, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

class MealOrderedLine(models.Model):
    meal     = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)