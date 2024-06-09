from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from cliente.models import Cliente

@receiver(post_save, sender=User)
def create_cliente_profile(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_cliente_profile(sender, instance, **kwargs):
    instance.cliente.save()
