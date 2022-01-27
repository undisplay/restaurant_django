import threading
import time

from django.conf import settings

def save_multi_db(model_class):
    
    def save_wrapper(save_func): 
        def new_save(self, *args, **kwargs):
            super(model_class, self).save(*args, **kwargs)
            if settings.PRODUCTION == None:
                
                def thread_function():
                    while True:
                        try:
                            super(model_class, self).save(*args, **kwargs,using='remote')
                            print("successfuly save:",self)
                            break
                        except:
                            time.sleep(2)
                
                th = threading.Thread(target=thread_function, daemon=True)            
        return new_save

    func = getattr(model_class, 'save')
    setattr(model_class, 'save', save_wrapper(func)) 

    return save_wrapper