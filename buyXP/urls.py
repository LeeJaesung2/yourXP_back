<<<<<<< HEAD
from django.urls import path
from .import views

urlpatterns = [
    
]
=======
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

>>>>>>> c2a8adb83ca1f428e054c54f1acdca866ec8f31d
