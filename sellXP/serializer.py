
from rest_framework import serializers
from .models import SellXP
from .models import Sell_review
from dataclasses import field

class SellXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellXP
        fields = ('s_id', 'title', 'text', 'create_time', 'user', 'hits', 'recommend', 'price', 'sellXP_tag')

class Sell_reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_review
        fields = '__all__'
        read_only_fields= ('sellXP_id', )

