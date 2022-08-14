from django.contrib import admin
from django.urls import path
from yourXP import views

URLPatterns = [
    path('admin', admin.site.urls),
    path('buys', views.getBuyById, name="getBuys"),
    path('buy', views.createBuy, name="createBuy"),
    path('buy/<buy_id>', views.getBuyById, name="getReviewById"),
    path('buy/<buy_id>', views.updateBuy, name="updateReview"),
    path('buy/<buy_id>', views.deleteBuy, name="deleteReview"),
]