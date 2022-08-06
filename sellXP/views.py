from functools import partial
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SellXPSerializer
from .serializer import Sell_reviewSerializer
from .models import SellXP
from .models import Sell_review
from sellXP import serializer
from django.contrib.auth.decorators import login_required
# Create your views here.

# SellXP CRUD 
@api_view(['GET'])
def getSellXP(request):
    sellxp = SellXP.objects.all()
    serializer = SellXPSerializer(sellxp, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createSellXP(request):
    serializer = SellXPSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
@login_required(login_url = '')
def sellXP_like(request, sellxp_id):
    sellxp = SellXP.objects.get(id = sellxp_id)
    user = request.user
    if sellxp.sellXP_like.filter(id=request.user.id).exists():
        sellxp.sellXP_like.remove(user)
        return JsonResponse({'message ': 'delete', 'sellXP_like_cnt':sellxp.sellxp_like.count()})
    else:
        sellxp.sellXP_like.add(user)
        return JsonResponse({'message ': 'ok', 'sellXP_like_cnt':sellxp.sellxp_like.count()})

# Create your views here.
@api_view(['GET'])
def getReviews(request, sellXP_id):
    sell_reviews = Sell_review.objects.filter(sellXP_id = sellXP_id)
    serializer = Sell_reviewSerializer(sell_reviews, many = True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def  reviewDetail(request, sellXP_id, sell_review_id):
    sell_review = Sell_review.objects.get(pk = sell_review_id)
    if request.method == 'GET':
        serializer = Sell_reviewSerializer(sell_review)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        print(request.data)
        serializer = Sell_reviewSerializer(sell_review, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sell_review.delete()
        return Response({'message':'sucess', 'code' : 200})

@api_view(['POST'])
def createReview(request, sellXP_id):
    sellXP = SellXP.objects.get(pk = sellXP_id)
    serializer = Sell_reviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sellXP_id=sellXP)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
