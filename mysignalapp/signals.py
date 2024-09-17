from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading


@receiver(post_save,sender=User)
def user_save(sender,instance,**kwargs):
    print(f'User save Instance {threading.get_ident()}')
    
    
    
    if instance.username == 'error_user':
        raise ValueError("Intentional error to test transaction rollback")