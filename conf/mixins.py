from django.db import models
from django.utils.translation import gettext_lazy as _

from conf import settings

import threading
import time
import logging

class SyncMixin(models.Model):
    # def save(self, *args, **kwargs):
    #     format = "%(asctime)s: %(message)s"
    #     logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
           
    #     super(SyncMixin, self).save(*args, **kwargs)
        
    #     if settings.PRODUCTION == None:
                
    #         def thread_function():
    #             while True:
    #                 try:
    #                     super(SyncMixin, self).save(*args, **kwargs,using='remote')
    #                     logging.info("successfuly save: %s",self)
    #                     break
    #                 except Exception as e:
    #                     logging.info(e)
    #                     time.sleep(2)
                        
    #         th = threading.Thread(target=thread_function)  
    #         th.start()
            
            

    class Meta:
        abstract = True

class StockMixin(models.Model):
    quantity_available = models.IntegerField(_('Quantity available'),help_text=_('Ex: 1'),blank=False,default=1)

    class Meta:
        abstract = True

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class MediaMixin(models.Model):
    image = models.ImageField(upload_to ='products/images/',null=True,blank=True)

    class Meta:
        abstract = True