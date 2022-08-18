from rest_framework import serializers
from .models import BuyXP

class BuyXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP
        fields = '__all__'


class hitsBuyXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyXP
        fields = ('hits')