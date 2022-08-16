from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    real_name = models.CharField(max_length=100, null=False)
    profile = models.ImageField(null=True, blank=True)
    nickname = models.CharField(max_length=100, unique = True)
    email = models.EmailField(max_length=100, unique = True)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.username