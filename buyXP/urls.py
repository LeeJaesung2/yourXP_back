from django.urls import path
from .import views

urlpatterns = [
    path('buys/hits', views.hitsGetBuyXP, name="getBuyXP"),
    path('buys/views', views.viewsGetBuyXP, name="getBuyXP"),
    path('buys/<str:search_keyword>', views.searchBuyXP, name='searchBuyXP'),
    path('buys/detail/<buyXP_id>', views.detailBuyXP, name="detailBuyXP"),
    path('buy', views.createBuyXP, name="createBuyXP"),
    path('buys/update/<buyXP_id>', views.updateBuyXP, name="updateBuyXP"),
    path('buys/delete/<int:buyXP_id>', views.deleteBuyXP, name="deleteBuyXP"),
]