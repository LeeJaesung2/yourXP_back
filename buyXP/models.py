from sqlite3 import DateFromTicks
from django.db import models

# Create your models here.

class BuyXP(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
#    user_id = models.ForeignKey("user_id", related_name="user") 
    deadline = models.TimeField()
    price = models.IntegerField()
    tag_id = models.ForeignKey("BuyXP_tag", related_name="tag", on_delete=models.CASCADE)
    hits = models.IntegerField()

#   조회수 기능 (프론트에서 함수호출 필요)
    @property
    def update_hit(self):
        self.hits = self.hits + 1
        self.save()

class BuyXP_tag(models.Model):
    tag1 = models.CharField(max_length=100, null=True)
    tag2 = models.CharField(max_length=100, null=True)
    tag3 = models.CharField(max_length=100, null=True)
    tag4 = models.CharField(max_length=100, null=True)
    tag5 = models.CharField(max_length=100, null=True)
    tag6 = models.CharField(max_length=100, null=True)
    tag7 = models.CharField(max_length=100, null=True)
    tag8 = models.CharField(max_length=100, null=True)