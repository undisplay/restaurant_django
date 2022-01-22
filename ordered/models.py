from django.db import models

from django.utils.translation import gettext_lazy as _

from conf.mixins import TimeStampMixin,MediaMixin

from employe.models import *
from drink.models import *
from food.models import *
from menu.models import *
from motel.models import *
from wash.models import *

class Ordered(TimeStampMixin,MediaMixin,models.Model):
    employe     = models.ForeignKey(Employe, on_delete=models.CASCADE)
    client      = models.CharField(_('Client Name'),help_text=_('Ex: John Doe'), max_length=150, blank=False)
    is_complete = models.BooleanField(_("Is Complete"),default=False,blank=False)

    def __str__(self):
        return 'Employe:(%s) Client:%s' % (self.employe,self.client)
    
    @property
    def total_price(self):
        total = 0
        
        for item in self.drinkorderedline_set.all():
            total += item.total_price
            
        for item in self.mealorderedline_set.all():
            total += item.total_price
            
        for item in self.washorderedline_set.all():
            total += item.total_price
            
        for item in self.roomorderedline_set.all():
            total += item.total_price
            
        return total

class DrinkOrderedLine(TimeStampMixin,MediaMixin,models.Model):
    ordered  = models.ForeignKey(Ordered, on_delete=models.CASCADE)
    drink    = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Ordered:(%s) Drink:(%s)' % (self.ordered,self.drink)
    
    @property
    def total_price(self):
        return self.drink.sale_price * self.quantity
    
    def save(self, *args, **kwargs):
        self.drink.quantity_available = int(self.drink.quantity_available) - int(self.quantity)
        self.drink.save()
        super(DrinkOrderedLine, self).save(*args, **kwargs)
        
    
class MealOrderedLine(TimeStampMixin,MediaMixin,models.Model):
    ordered  = models.ForeignKey(Ordered, on_delete=models.CASCADE)
    meal     = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Ordered:(%s) Meal:(%s)' % (self.ordered,self.meal)
    
    @property
    def total_price(self):
        return self.meal.sale_price * self.quantity
    
    def save(self, *args, **kwargs):
        self.meal.quantity_available = int(self.meal.quantity_available) - int(self.quantity)
        self.meal.save()
        super(MealOrderedLine, self).save(*args, **kwargs)

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
    
    @property
    def total_price(self):
        return self.wash.wash_price * self.quantity
    
class RoomOrderedLine(TimeStampMixin,MediaMixin,models.Model):
    ordered  = models.ForeignKey(Ordered, on_delete=models.CASCADE)
    room     = models.ForeignKey(Room, on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'),help_text=_('Ex: 1'),blank=False,default=1)

    def __str__(self):
        return 'Ordered:(%s) Room:(%s)' % (self.ordered,self.room)
    
    @property
    def total_price(self):
        return self.room.loan_price * self.quantity
    