from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save,sender=User)
def user_save(sender,instance,**kwargs):
    print('User save Instance')