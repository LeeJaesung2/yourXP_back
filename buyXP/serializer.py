from rest_framework import serializers
from .models import BuyXP, BuyXP_tag

class BuyXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP
        fields = ('id', 'title', 'text', 'create_time', 'hits', 'price', 'BuyXP_tag', 'user_id') 

class BuyXP_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP_tag
        fields = ('tag1', 'tag2','tag3','tag4','tag5','tag6','tag7','tag8') 
