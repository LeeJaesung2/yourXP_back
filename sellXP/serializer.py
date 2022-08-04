from dataclasses import field
from rest_framework import serializers
from .models import SellXP
from .models import Sell_review

class SellXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellXP
        fields = '__all__'

class Sell_reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_review
        fields = '__all__'
        read_only_fields= ('sellXP_id', )