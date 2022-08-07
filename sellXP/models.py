from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User

class SellXP_tag(models.Model):
    tag1 = models.CharField(max_length=100, null=True)
    tag2 = models.CharField(max_length=100, null=True)
    tag3 = models.CharField(max_length=100, null=True)
    tag4 = models.CharField(max_length=100, null=True)
    tag5 = models.CharField(max_length=100, null=True)
    tag6 = models.CharField(max_length=100, null=True)
    tag7 = models.CharField(max_length=100, null=True)
    tag8 = models.CharField(max_length=100, null=True)
    tag9 = models.CharField(max_length=100, null=True)
    tag10 = models.CharField(max_length=100, null=True)

# Create your models here.
class SellXP(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, default="", blank=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    recommend = models.PositiveIntegerField(default=0)
    price = models.IntegerField()
    sellXP_tag = models.ForeignKey(SellXP_tag, related_name='+', on_delete=models.CASCADE, default="", blank=True, null=True)
    # 좋아요 기능 N:N 관계정의
    like = models.ManyToManyField(User, related_name="likes", blank=True)

class Sell_review(models.Model):
    sellXP_id = models.ForeignKey("SellXP", related_name="sellXP", on_delete=models.CASCADE, db_column="sellXP_id")
    body = models.TextField()
    user_id = models.CharField(max_length=100)
    grad = models.IntegerField(null=False, validators=[MaxValueValidator(10),MinValueValidator(1)])

