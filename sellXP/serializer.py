from rest_framework import serializers
from .models import SellXP, Sell_review, Sell_image

class SellXPSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.image.all() 
        return Sell_imageSerializer(image, many=True, context=self.context).data
    
    class Meta:
        model = SellXP
        fields = ('id','title','text','create_time','user','hits','recommend','price', 'images','tag1','tag2','tag3','tag4','tag5','tag6','tag7','tag8','tag9','tag10')

    def create(self, validated_data):
        instance  = SellXP.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            Sell_image.objects.create(sellXP_id=instance, image=image_data)
        return instance 

class Sell_imageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Sell_image
        fields = ['image']

class Sell_reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_review
        fields = '__all__'
        read_only_fields= ('sellXP_id', )