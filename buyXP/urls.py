from django.contrib import admin
from django.urls import path
from buyXP import views

urlpatterns = [
    path('buys', views.getBuyXP, name="getBuyXP"),
    path('buy', views.createBuyXP, name="createBuyXP"),
]

