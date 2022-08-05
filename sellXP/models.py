from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User

class SellXP_tag(models.Model):
    pass

# Create your models here.
class SellXP(models.Model):
    #s_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, default="", blank=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    recommend = models.PositiveIntegerField(default=0)
    price = models.IntegerField()
    sellXP_tag = models.ForeignKey(SellXP_tag, related_name='+', on_delete=models.CASCADE, default="", blank=True, null=True)


class Sell_review(models.Model):
    sellXP_id = models.ForeignKey("SellXP", related_name="sellXP", on_delete=models.CASCADE, db_column="sellXP_id")
    body = models.TextField()
    user_id = models.CharField(max_length=100)
    grad = models.IntegerField(null=False, validators=[MaxValueValidator(10),MinValueValidator(1)])

