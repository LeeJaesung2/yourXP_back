from dataclasses import field
from rest_framework import serializers
from .models import Post
from .models import Review

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'contents', 'author', 'pub_date')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','post_id', 'comment', 'author', 'star', 'pub_date')
        read_only_fields= ('post', )