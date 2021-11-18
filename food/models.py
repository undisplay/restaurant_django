from django.db import models

from django.utils.translation import gettext_lazy as _

class Meal(models.Model):
    name          = models.CharField(_('Name'),help_text='Ex:Buger',unique=True, max_length=150, blank=False)
    price         = models.DecimalField(_('Price'),help_text=_('Ex: 300'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    sale_price    = models.DecimalField(_('Sale Price'),help_text=_('Ex: 30'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    type          = models.CharField(_('Type'),help_text='Ex:Main', max_length=150, blank=False)