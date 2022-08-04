from rest_framework import serializers
from .models import buyXP

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = buyXP
        fields = ('id', 'title', 'body', 'due_date', 'point', 'pub_date')
