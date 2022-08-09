from rest_framework import serializers
from .models import SellXP, SellXP_tag
from .models import Sell_review
from dataclasses import field

class SellXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellXP
        fields = ('id', 'title', 'text', 'hits', 'recommend', 'price')

class Sell_reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_review
        fields = '__all__'
        read_only_fields= ('sellXP_id', )

class SellXP_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellXP_tag
        fields = ('tag1', 'tag2','tag3','tag4','tag5','tag6','tag7','tag8','tag9','tag10')

