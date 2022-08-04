from rest_framework import serializers
from .models import BuyXP, BuyXP_tag

class BuyXpSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP
        fields = ('id', 'title', 'text', 'create_time', 'user_id', 'hits', 'price', 'tag_id')

class BuyXP_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP_tag
        fields = ('tag_id','tag1', 'tag2','tag3','tag4','tag5','tag6','tag7','tag8') 
