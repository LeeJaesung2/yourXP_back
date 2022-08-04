from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import buyXP
from .serializer import BuySerializer
from sellXP import serializer


# Create your views here.
@api_view(['GET'])
def getBuyById(request):
    buys = buyXP.objects.all()
    serializer = BuySerializer(buys, many=True)
    return response(serializer.data)
