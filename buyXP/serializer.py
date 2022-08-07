from rest_framework import serializers
from .models import BuyXP, BuyXP_tag

class BuyXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP
        fields = ('id', 'title', 'text', 'create_time', 'hits', 'price', 'tag_id') # 나중에 user_id 넣기

class BuyXP_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP_tag
        fields = ('tag_id','tag1', 'tag2','tag3','tag4','tag5','tag6','tag7','tag8') 
