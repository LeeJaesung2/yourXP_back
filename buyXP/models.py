from sqlite3 import DateFromTicks
from django.db import models

# Create your models here.
class Writer(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField
    due_date = models.TimeField
    point = models.IntegerField
    pub_date = models.DateTimeField(auto_now_add=True)



class Buy(models.Model):
    id = models.BigAutoField(primary_key=True)
    buy_id = models.ForeignKey("Writer", related_name="writers", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
