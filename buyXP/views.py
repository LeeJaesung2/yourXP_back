from dataclasses import field
from functools import partial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib import response
from .models import BuyXP, BuyXP_tag
from .serializer import BuyXP_tagSerializer, BuyXPSerializer
from buyXP import serializer
from user.models import User
from operator import itemgetter, attrgetter
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

#불러오기 BuyXP와 BuyXP_tag 동시에 불러오는 것으로 수정하는 중 BuyXP_tag도 같이 로딩되도록 모두 수정함
@api_view(['GET'])
def getBuyXP(request):
    buys = BuyXP.objects.all()
    if request.method == 'GET':
        buysSerializer = BuyXPSerializer(buys, many=True)
        return Response(buysSerializer.data)
    
@api_view(['GET'])
def searchBuyXP(request, searchName):
        name = searchName
        buys = BuyXP.objects.all()
        searchBuys = buys.filter(title__icontains=name)
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
    tags = BuyXP_tag.objects.get(pk=buyXP_id)
    buys = BuyXP.objects.get(pk=buyXP_id) 
    buysSerializer = BuyXPSerializer(buys, data=request.data, partial=True)
    tagsSerializer = BuyXP_tagSerializer(tags, data=request.data, partial=True)
    serializer = buysSerializer, tagsSerializer
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteBuyXP(request, buyXP_id):
    buys = BuyXP.objects.get(pk=buyXP_id)
    buys.delete()
    tags = BuyXP_tag.objects.get(pk=buyXP_id)
    tags.delete()
    return Response({'message':'success', 'code':'200'})

### 필요없는 부분 ###

#drf 검색 폼 코드 (template 필요해서 주석 처리함)
# class searchBuyXPList(generics.ListAPIView):
#     queryset = BuyXP.objects.all()
#     serializer_class = BuyXPSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'text']




# # Create your views here.
# class SearchListCreateView(ListCreateAPIView):
#     name = "board-list-create"
#     serializer_class = BuyXP
    
#     def searchBuyXP(self):
#         buys = BuyXP.objects.all()
#         return buys

#     def list(self, request, *args, **kwargs):
#         buysSearchlist = self.set_filters( self.searchBuyXP(), request )

#         serializer = self.get_serializer(buysSearchlist, many=True)
        
#         return Response(serializer.data)

#     def set_filters(self, queryset, request):        
#         type = request.query_params.get('type', None)
#         description = request.query_params.get('description', None)

#         if type is not None:
#             queryset = queryset.filter(type=type)
        
#         if description is not None:
#             queryset = queryset.filter(description__contains=description)

#         return queryset


# class BuyXPRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     name = "buyXP-retrieve-update-destroy"
#     serializer_class = BuyXPSerializer
#     buys = BuyXP.objects.all()


# @api_view(['GET'])
# def pointsBuyXP(request):
#     buys = BuyXP.objects.all()
#     hit = BuyXP.hits
#     sorted(buys, key=attrgetter(hit), reverse=True)
#     buysSerializer = BuyXPSerializer(buys, many=True)
#     return Response(buysSerializer.data)