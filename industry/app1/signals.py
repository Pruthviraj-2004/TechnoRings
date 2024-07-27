from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ShedDetails, ShedUser

@receiver(post_save, sender=ShedDetails)
def create_or_update_user_and_sheduser(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.name, password=instance.password)
        ShedUser.objects.create(user=user, shed=instance)
    else:
        user = User.objects.get(username=instance.name)
        if instance.password != user.password:
            user.set_password(instance.password)
            user.save()