from functools import partial
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SellXPSerializer
from .serializer import Sell_reviewSerializer
from .models import SellXP
from .models import Sell_review
from sellXP import serializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

# SellXP CRUD
@api_view(['GET'])
def getSellXPs(request):
    sellxp = SellXP.objects.all()
    serializer = SellXPSerializer(sellxp, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getSellXP(request, sellXP_id):
    sellxp = SellXP.objects.get(pk = sellXP_id)
    serializer = SellXPSerializer(sellxp, context={"request": request})
    return Response(serializer.data)

@api_view(['POST'])
def createSellXP(request):
    serializer = SellXPSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
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

class sellXPViewSet(ModelViewSet):
    queryset = SellXP.objects.all().order_by('-create_time')
    serializer_class = SellXPSerializer