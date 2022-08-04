from django.db import models
class TestModel(models.Model):
    pass

# Create your models here.
class Posts(models.Model):
    s_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(TestModel, related_name='+', on_delete=models.CASCADE, default="", blank=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    recommend = models.PositiveIntegerField(default=0)
    price = models.IntegerField()
    sellXP_tag = models.ForeignKey(TestModel, related_name='+', on_delete=models.CASCADE, default="", blank=True, null=True)

