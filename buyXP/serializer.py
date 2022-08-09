from rest_framework import serializers
from .models import BuyXP, BuyXP_tag

class BuyXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP
        fields = ('title', 'hits', 'create_time', 'user_id', 'text', 'price', 'BuyXP_tag') 

class BuyXP_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP_tag
        fields = ('tag1', 'tag2','tag3','tag4','tag5','tag6','tag7','tag8') 
