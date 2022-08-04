from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('s_id', 'title', 'text', 'create_time', 'user', 'hits', 'recommend', 'price', 'sellXP_tag')