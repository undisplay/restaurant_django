from django.db import models

from django.utils.translation import gettext_lazy as _

from food.models import *
from drink.models import *

class Menu(models.Model):
    name          = models.CharField(_('Name'),help_text='Ex:Coca',unique=True, max_length=150, blank=False)
    discount      = models.DecimalField(_('Discount(%)'),help_text=_('Ex: 30'),max_length=255,max_digits=11,decimal_places=2,blank=False)

    def __str__(self):
        return 'Name:%s' % (self.name)

class MenuMeal(models.Model):
    meal     = models.ForeignKey(Meal, on_delete=models.CASCADE)
    menu     = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Menu:(%s) Meal:(%s)' % (self.menu,self.meal)

class MenuDrink(models.Model):
    drink    = models.ForeignKey(Drink, on_delete=models.CASCADE)
    menu     = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Menu:(%s) Drink:(%s)' % (self.menu,self.drink)
