from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser 

from django.utils.translation import gettext_lazy as _

class Winegrower(models.Model):
    first_name  = models.CharField(_('Firstname'),help_text='Ex:john', max_length=150, null=True,blank=False)
    last_name   = models.CharField(_('Lastname'),help_text='Ex:snow', max_length=150, null=True,blank=False)
    phone       = PhoneNumberField(_('Phone'),help_text='Ex:+509XXXXXXXX',blank=True,max_length=15)
    address     = models.TextField(_('Address'),help_text=_('Entrer address'),blank=True,null=True)

class Wine(models.Model):
    winegrower    = models.ForeignKey(Winegrower, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(_("creation date"),blank=False)
    price         = models.DecimalField(_('Price'),help_text=_('Ex: 300'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    sale_price    = models.DecimalField(_('Sale Price'),help_text=_('Ex: 30'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    buy_date      = models.DateTimeField(_("Buy date"),blank=False)
    type          = models.CharField(_('Type'),help_text='Ex:Rouge', max_length=150, blank=False)
    name          = models.CharField(_('Name'),help_text='Ex:Bordeaux',unique=True, max_length=150, blank=False)

class Drink(models.Model):
    name          = models.CharField(_('Name'),help_text='Ex:Coca',unique=True, max_length=150, blank=False)
    price         = models.DecimalField(_('Price'),help_text=_('Ex: 300'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    sale_price    = models.DecimalField(_('Sale Price'),help_text=_('Ex: 30'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    type          = models.CharField(_('Type'),help_text='Ex:Main', max_length=150, blank=False)