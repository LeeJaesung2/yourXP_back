from dataclasses import field
from functools import partial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib import response
from .models import BuyXP
from .serializer import BuyXPSerializer, hitsBuyXPSerializer
from buyXP import serializer
from user.models import User
from operator import itemgetter, attrgetter
from rest_framework import generics
from django.shortcuts import render
from rest_framework.filters import SearchFilter


# Create your views here.

#불러오기 BuyXP와 BuyXP_tag 동시에 불러오는 것으로 수정하는 중 BuyXP_tag도 같이 로딩되도록 모두 수정함
@api_view(['GET'])
def hitsGetBuyXP(request):
    buys = BuyXP.objects.all().order_by('-hits')
    if request.method == 'GET':
        buysSerializer = BuyXPSerializer(buys, many=True)
        return Response(buysSerializer.data)

@api_view(['GET'])
def viewsGetBuyXP(request):
    buys = BuyXP.objects.all().order_by('-id')
    if request.method == 'GET':
        buysSerializer = BuyXPSerializer(buys, many=True)
        return Response(buysSerializer.data)
    
@api_view(['GET'])
def searchBuyXP(request, search_keyword):
        name = request
        buys = BuyXP.objects.all()
        searchBuys = buys.filter(title__icontains=search_keyword)
        searchBuysSerializer = BuyXPSerializer(searchBuys, many=True)
        return Response(searchBuysSerializer.data)

#디테일
@api_view(['GET'])
def detailBuyXP(request, buyXP_id):
    buys = BuyXP.objects.get(pk=buyXP_id)
    buysSerializer = BuyXPSerializer(buys)
    return Response(buysSerializer.data)

#크리에이트
@api_view(['POST'])
def createBuyXP(request):
    serializer = BuyXPSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update
@api_view(['PATCH'])
def updateBuyXP(request, buyXP_id):
    print(request.data)
    buys = BuyXP.objects.get(pk=buyXP_id) 
    buysSerializer = BuyXPSerializer(buys, data=request.data, partial=True)
    if buysSerializer.is_valid():
        buysSerializer.save()
        return Response(buysSerializer.data, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteBuyXP(request, buyXP_id):
    buys = BuyXP.objects.get(pk=buyXP_id)
    buys.delete()
    return Response({'message':'success', 'code':'200'})

