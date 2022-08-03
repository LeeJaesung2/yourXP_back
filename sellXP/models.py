from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    title = models.CharField(help_text="Post title", max_length=100, null = True)
    contents = models.TextField(help_text="post contents")
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    id = models.BigAutoField(help_text="Review ID", primary_key=True)
    post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")
    comment = models.TextField()
    author = models.CharField(max_length=100)
    star = models.IntegerField(null=False, validators=[MaxValueValidator(10),MinValueValidator(1)])
    pub_date = models.DateTimeField(auto_now_add=True)