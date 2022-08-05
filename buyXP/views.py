from dataclasses import field
from functools import partial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib import response
from .models import BuyXP, BuyXP_tag
from .serializer import BuyXP_tagSerializer, BuyXPSerializer
from buyXP import serializer


# Create your views here.

#불러오기 BuyXP와 BuyXP_tag 동시에 불러오는 것으로 수정하는 중 (현재는 BuyXP만 불러오기 함)
@api_view(['GET'])
def getBuyXP(request):
    buys = BuyXP.objects.all()
    tags = BuyXP_tag.objects.all()
    buysSerializer = BuyXPSerializer(buys, many=True)
    tagsSerializer = BuyXP_tagSerializer(tags, many=True)
    return Response(buysSerializer.data), Response(tagsSerializer.data)


@api_view(['GET'])
def detailBuyXP(request):
    buys = BuyXP.objects.get(pk=id)
    tags = BuyXP_tag.objects.get(pk=id)
    buysSerializer = BuyXPSerializer(buys)
    tagsSerializer = BuyXP_tagSerializer(tags)
    serializer = buysSerializer, tagsSerializer
    if serializer.is_valid():
        return Response(buysSerializer.data, tagsSerializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createBuyXP(request):
    serializer = BuyXPSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH'])
def updateBuyXP(request):
    print(request.data)
    buys = BuyXP.objects.get(pk=id) 
    serializer = BuyXPSerializer(buys, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteBuyXP(request):
    buys = BuyXP.objects.get(pk=id)
    buys.delete()
    return Response({'message':'success', 'code':'200'})