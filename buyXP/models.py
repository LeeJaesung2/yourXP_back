from sqlite3 import DateFromTicks
from django.db import models

# Create your models here.

class BuyXP(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey("user_id", related_name="user") 
    deadline = models.DateTimeField()
    price = models.IntegerField()
    BuyXP_tag = models.ForeignKey("BuyXP_tag", related_name="+", on_delete=models.CASCADE, default="", blank=True, null=True)

    hits = models.IntegerField()

class BuyXP_tag(models.Model):
    tag1 = models.CharField(max_length=100, null=True)
    tag2 = models.CharField(max_length=100, null=True)
    tag3 = models.CharField(max_length=100, null=True)
    tag4 = models.CharField(max_length=100, null=True)
    tag5 = models.CharField(max_length=100, null=True)
    tag6 = models.CharField(max_length=100, null=True)
    tag7 = models.CharField(max_length=100, null=True)
    tag8 = models.CharField(max_length=100, null=True)