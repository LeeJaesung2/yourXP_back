from functools import partial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib import response
from .models import BuyXP, BuyXP_tag
from .serializer import BuyXPSerializer
from buyXP import serializer


# Create your views here.
@api_view(['GET'])
def getBuyXP(request):
    buys = BuyXP.objects.all()
    serializer = BuyXPSerializer(buys, many=True)
    return Response(serializer.data)

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