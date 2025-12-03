from django.dispatch import receiver
from djoser.signals import user_registered as registration_signal
from ..models import Profile

@receiver(registration_signal)
def user_registered(sender, **kwargs):
    print('-' * 15)
    print(f"user Registred: {kwargs['user']}")
    new_user_profile = Profile(user=kwargs['user'])
    new_user_profile.save()
    print('-' * 15)

    pass