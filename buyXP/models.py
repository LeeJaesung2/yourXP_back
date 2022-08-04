from sqlite3 import DateFromTicks
from django.db import models

# Create your models here.

class buyXP(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
#    user_id = models.ForeignKey("user_id", related_name="user")
    hits = models.IntegerField()
    deadline = models.TimeField()
    price = models.IntegerField()
    tag_id = models.ForeignKey("buyXP_tag", related_name="tag", on_delete=models.CASCADE)
    hits = models.IntegerField()

class buyXP_tag(models.Model):
    tag_id = models.IntegerField()
    tag1 = models.CharField(max_length=100)
    tag2 = models.CharField(max_length=100)
    tag3 = models.CharField(max_length=100)
    tag4 = models.CharField(max_length=100)
    tag5 = models.CharField(max_length=100)
    tag6 = models.CharField(max_length=100)
    tag7 = models.CharField(max_length=100)
    tag8 = models.CharField(max_length=100)