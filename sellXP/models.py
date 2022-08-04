from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class SellXP(models.Model):
    title = models.CharField(help_text="Post title", max_length=100, null = True)
    text = models.TextField(help_text="post text")
    create_time = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=100)
    hits = models.IntegerField()
    recommend = models.IntegerField()
    price = models.IntegerField()
    tag_id = models.IntegerField()

class Sell_review(models.Model):
    sellXP_id = models.ForeignKey("SellXP", related_name="sellXP", on_delete=models.CASCADE, db_column="sellXP_id")
    body = models.TextField()
    user_id = models.CharField(max_length=100)
    grad = models.IntegerField(null=False, validators=[MaxValueValidator(10),MinValueValidator(1)])