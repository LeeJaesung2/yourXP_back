from django.shortcuts import render
from .models import Buy

# Create your views here.
def index(request):
    buys = Buy.objects.all()
    return render(request, 'buylist.html', {'buys':buys})

def detail(request):
    buy_detail = Buy.objects.all(Buy, pk=buy_id)
    return render(request, 'buydetail.html', {'buy_detail':buy_detail})
    #ffasada
