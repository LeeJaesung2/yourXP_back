from sqlite3 import DateFromTicks
from django.db import models
from user.models import User

# Create your models here.

class BuyXP(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, default="", null=True, blank=True)
    deadline = models.DateTimeField()
    price = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(default=0)
    tag1 = models.CharField(max_length=100, blank=True, null=True)
    tag2 = models.CharField(max_length=100, blank=True, null=True)
    tag3 = models.CharField(max_length=100, blank=True, null=True)
    tag4 = models.CharField(max_length=100, blank=True, null=True)
    tag5 = models.CharField(max_length=100, blank=True, null=True)
    tag6 = models.CharField(max_length=100, blank=True, null=True)
    tag7 = models.CharField(max_length=100, blank=True, null=True)
    tag8 = models.CharField(max_length=100, blank=True, null=True)
    tag9 = models.CharField(max_length=100, blank=True, null=True)
    tag10 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

#   조회수 기능 (프론트에서 함수호출 필요)
    @property
    def update_hit(self):
        self.hits = self.hits + 1
        self.save()
