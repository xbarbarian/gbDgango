from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(
        User,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE,
    )

    tagline = models.CharField(
        verbose_name='тэги',
        max_length=128,
        blank=True,
    )

    about_me = models.TextField(
        verbose_name='о себе',
        max_length=512,
        blank=True,
    )

    gender = models.CharField(
        verbose_name='пол',
        choices=GENDER_CHOICES,
        blank=True,
        max_length=128,
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
