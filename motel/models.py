from django.db import models

from conf.mixins import TimeStampMixin,MediaMixin

from django.utils.translation import gettext_lazy as _

class Room(TimeStampMixin,MediaMixin,models.Model): 
    loan_price    = models.DecimalField(_('Price'),help_text=_('Ex: 300'),max_length=255,max_digits=11,decimal_places=2,blank=False)
    number        = models.CharField(_('Number'),help_text='Ex: CH1',max_length=255,blank=False)
    created_at    = models.DateTimeField(_("entry date"),auto_now=True,blank=False)
    
    def __str__(self):
        return 'Number:%s Price:%s' % (self.number,self.loan_price)
