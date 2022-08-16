from django.contrib import admin
from django.urls import path
from .import views
#후
urlpatterns = [
    path('admin', admin.site.urls),
    #path('buys', views.getBuyById, name="getBuys"),
    #path('buy', views.createBuy, name="createBuy"),
    #path('buy/<buy_id>', views.getBuyById, name="getReviewById"),
    #path('buy/<buy_id>', views.updateBuy, name="updateReview"),
    #path('buy/<buy_id>', views.deleteBuy, name="deleteReview"),
#전
    path('buys', views.getBuyXP, name="getBuyXP"),
    path('buys/detail/<id>', views.detailBuyXP, name="detailBuyXP"),
    path('buy', views.createBuyXP, name="createBuyXP"),
    path('buys/update/<id>', views.updateBuyXP, name="updateBuyXP"),
]