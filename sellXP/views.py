from functools import partial
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SellXPSerializer, Sell_reviewSerializer
from .models import SellXP, Sell_review
from sellXP import serializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.decorators import login_required
from .models import User
from datetime import date, datetime, timedelta

# Create your views here.

# SellXP CRUD 
@api_view(['GET'])
def viewsGetSellXPs(request):
    sellxp = SellXP.objects.all().order_by('-id')
    serializer = SellXPSerializer(sellxp, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def viewsGetSellXPsRank(request):
    sellxp = SellXP.objects.all().order_by('-hits')[:3]
    serializer = SellXPSerializer(sellxp, many = True)
    return Response(serializer.data)

# @api_view(['GET'])
# def recommendsGetSellXPs(request):
#     likecount = len(SellXP.objects.like)
#     sellxp = SellXP.objects.all().order_by('-likecount')
#     serializer = SellXPSerializer(sellxp, many = True)
#     return Response(serializer.data)

@api_view(['GET'])
def getSellXP(request, sellXP_id):
    sellxp = SellXP.objects.get(pk = sellXP_id)
    serializer = SellXPSerializer(sellxp, context={"request": request})
    return Response(serializer.data)

class sellXPViewSet(ModelViewSet):
    queryset = SellXP.objects.all().order_by('-create_time')
    serializer_class = SellXPSerializer

@api_view(['PATCH'])
def updateSellXP(request, sellxp_id):
    sellxp = SellXP.objects.get(pk = sellxp_id)
    serializer = SellXPSerializer(sellxp, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteSellXP(request, sellxp_id):
    sellxp = SellXP.objects.get(pk = sellxp_id)
    sellxp.delete()
    return Response({'message':'sucess', 'code' : 200})

# 좋아요 기능 구현 (비동기 통신), js코드로 ajax방식으로 표현 필요
@login_required(login_url = '/user/login')
def sellXP_like(request, sellxp_id):
    sellxp = SellXP.objects.get(id = sellxp_id)
    user = request.User
    if sellxp.sellXP_like.filter(id=request.user.id).exists():
        sellxp.sellXP_like.remove(user)
        return JsonResponse({'message ': 'delete', 'sellXP_like_cnt':sellxp.sellxp_like.count()})
    else:
        sellxp.sellXP_like.add(user)
        return JsonResponse({'message ': 'ok', 'sellXP_like_cnt':sellxp.sellxp_like.count()})

@api_view(['GET'])
def getReviews(request, sellXP_id): #해당 글의 리뷰 전체 보기
    sell_reviews = Sell_review.objects.filter(sellXP_id = sellXP_id)
    serializer = Sell_reviewSerializer(sell_reviews, many = True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def  reviewDetail(request, sellXP_id, sell_review_id): #한 리뷰 보기, 수정, 삭제
    sell_review = Sell_review.objects.get(pk = sell_review_id)
    if request.method == 'GET':
        serializer = Sell_reviewSerializer(sell_review)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        print(request.data)
        serializer = Sell_reviewSerializer(sell_review, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sell_review.delete()
        return Response({'message':'sucess', 'code' : 200})

@api_view(['POST'])
def createReview(request, sellXP_id): #리뷰 작성
    sellXP = SellXP.objects.get(pk = sellXP_id)
    serializer = Sell_reviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sellXP_id=sellXP)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#검색 기능
@api_view(['GET'])
def searchSellXP(request, sellName):
    sells = SellXP.objects.all()
    searchSells = sells.filter(title__icontains=sellName)
    searchSellsSerializer = SellXPSerializer(searchSells, many=True)
    return Response(searchSellsSerializer.data)


