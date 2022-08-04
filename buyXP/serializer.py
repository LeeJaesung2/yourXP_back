from rest_framework import serializers
from .models import Buy, Writer

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ('id', 'title', 'body', 'due_date', 'point', 'pub_date')

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = ('id', 'buy_id', 'author', 'pub_date')