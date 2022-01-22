from django.db import models

from conf.mixins import TimeStampMixin,MediaMixin

from django.utils.translation import gettext_lazy as _

class Wash(TimeStampMixin,MediaMixin,models.Model): 
    wash_price    = models.DecimalField(_('Price'),help_text=_('Ex: 300'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    type          = models.CharField(_('Type'),help_text='Ex:Car',max_length=255,blank=False)
    
    def __str__(self):
        return 'Type:%s Price:%s' % (self.type,self.wash_price)
