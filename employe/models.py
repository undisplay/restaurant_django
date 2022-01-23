from django.db import models

from django.contrib.auth.models import AbstractUser 
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _

from conf.mixins import TimeStampMixin,MediaMixin

class Restaurant(TimeStampMixin,MediaMixin,models.Model):
    name        = models.CharField(_('Name'),help_text='Ex:Extaz',unique=True, max_length=150, blank=False)
    phone1      = PhoneNumberField(_('Phone'),help_text='Ex:+509XXXXXXXX',blank=False,max_length=15)
    phone2      = PhoneNumberField(_('Phone'),help_text='Ex:+509XXXXXXXX',blank=True,max_length=15)
    address     = models.TextField(_('Address'),help_text=_('Entrer address'),blank=True,null=True)

    def __str__(self):
        return 'Name:%s' % (self.name)
    
class Employe(TimeStampMixin,MediaMixin,AbstractUser):
    phone       = PhoneNumberField(_('Phone'),help_text='Ex:+509XXXXXXXX',blank=True,max_length=15)
    address     = models.TextField(_('Address'),help_text=_('Entrer address'),blank=True,null=True)
    restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return 'Firstname:%s Lastname:%s' % (self.first_name,self.last_name)
