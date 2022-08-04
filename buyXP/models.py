from sqlite3 import DateFromTicks
from django.db import models

# Create your models here.
class Writer(models.Model):
    b_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    deadline = models.TimeField()
    price = models.IntegerField()
    hits = models.IntegerField()



class Buy(models.Model):
    b_id = models.BigAutoField(primary_key=True)
    tag_id = models.ForeignKey("Writer", related_name="writers", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

