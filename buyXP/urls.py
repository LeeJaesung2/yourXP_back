from django.contrib import admin
from django.urls import path
from buyXP import views

urlpatterns = [
    path('buys', views.getBuyXP, name="getBuyXP"),
    path('buys/detail/<id>', views.detailBuyXP, name="detailBuyXP"),
    path('buy', views.createBuyXP, name="createBuyXP"),
    path('buys/update/<id>', views.updateBuyXP, name="updateBuyXP"),
]

