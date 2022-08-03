from ctypes import pointer
from email.quoprimime import body_check
from django.conf import DEFAULT_HASHING_ALGORITHM_DEPRECATED_MSG
from django.db import models

# Create your models here.
class Buy(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField
    hash_tag = models.CharField(max_length=10)
    body = models.TextField
    point = models.IntegerField
    due_date = models.DateField.auto_now
    image = models.ImageField

    def __str__(self):
        return self.title