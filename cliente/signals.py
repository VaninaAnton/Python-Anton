from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Realizar acciones adicionales cuando se crea un usuario
        pass
    else:
        # Realizar acciones adicionales cuando se actualiza un usuario
        pass
