from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User


class SellXP(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, default="", blank=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    recommend = models.PositiveIntegerField(default=0)
    price = models.IntegerField()
    # 좋아요 기능 N:N 관계정의
    tag1 = models.CharField(max_length=100, null=True, blank=True)
    tag2 = models.CharField(max_length=100, null=True, blank=True)
    tag3 = models.CharField(max_length=100, null=True, blank=True)
    tag4 = models.CharField(max_length=100, null=True, blank=True)
    tag5 = models.CharField(max_length=100, null=True, blank=True)
    tag6 = models.CharField(max_length=100, null=True, blank=True)
    tag7 = models.CharField(max_length=100, null=True, blank=True)
    tag8 = models.CharField(max_length=100, null=True, blank=True)
    tag9 = models.CharField(max_length=100, null=True, blank=True)
    tag10 = models.CharField(max_length=100, null=True, blank=True)
    like = models.ManyToManyField(User, related_name="likes", blank=True, null=True)
    def __str__(self):
        return self.title

def image_upload_path(instance, filename):
    return f'{instance.sellXP_id.id}/{filename}'

class Sell_image(models.Model):
    sellXP_id = models.ForeignKey("SellXP", related_name="image", on_delete=models.CASCADE, db_column="image_sellXP_id")
    image = models.ImageField(upload_to = image_upload_path)
    def __str__(self):
        return self.sellXP_id.title

# 조회수 기능 (프론트에서 함수호출 필요)
@property
def update_hit(self):
    self.hits = self.hits + 1
    self.save()

class Sell_review(models.Model): #리뷰 모델
    sellXP_id = models.ForeignKey("SellXP", related_name="sellXP", on_delete=models.CASCADE, db_column="sellXP_id")
    body = models.TextField()
    user = models.ForeignKey("user.User", related_name="user", on_delete=models.CASCADE, db_column="user")
    grad = models.FloatField(null=False, validators=[MaxValueValidator(10),MinValueValidator(1)])
    def __str__(self):
        return self.sellXP_id.title

