from django.db import models
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

