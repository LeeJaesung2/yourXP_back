from django.contrib import admin
from django.urls import path
from .import views
from buyXP import views

urlpatterns = [
    path('buys', views.getBuyXP, name="getBuyXP"),
    path('buys/detail/<buyXP_id>', views.detailBuyXP, name="detailBuyXP"),
    path('buy', views.createBuyXP, name="createBuyXP"),
    path('buys/update/<buyXP_id>', views.updateBuyXP, name="updateBuyXP"),
    path('buys/delete/<int:buyXP_id>', views.deleteBuyXP, name="deleteBuyXP"),
]

