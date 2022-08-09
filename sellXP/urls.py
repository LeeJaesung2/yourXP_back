from django.urls import path
from . import views

urlpatterns = [
    path('', views.getSellXPs, name="getSellXPs"),
    path('<sellXP_id>', views.getSellXP, name="getSellXP"),
    path('create', views.createSellXP, name="createSellXP"),
    path('update/<sellxp_id>', views.updateSellXP, name="updateSellXP"),
    path('delete/<int:sellxp_id>', views.deleteSellXP, name="deleteSellXP"),
    path('<sellXP_id>/reviews', views.getReviews, name="getReviews"),
    path('<sellXP_id>/review', views.createReview, name="createReview"),
    path('<sellXP_id>/review/<sell_review_id>', views.reviewDetail, name="readUpdateDelete"),
]