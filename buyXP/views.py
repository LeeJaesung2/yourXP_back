from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib import response
from .models import BuyXP
from .serializer import BuyXPSerializer


# Create your views here.
@api_view(['GET'])
def getBuyXP(request):
    buys = BuyXP.objects.all()
    serializer = BuyXPSerializer(buys, many=True)
    return Response(serializer.data)

