from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    group = models.ForeignKey(
        verbose_name='Group',
        to='application.Group',
        on_delete=models.PROTECT,
        related_name='users'
    )
