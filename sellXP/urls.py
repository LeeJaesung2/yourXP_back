from django.urls import path
from .import views

urlpatterns = [
    path('<post_id>/reviews', views.getReviews, name="getReviews"),
    path('<post_id>/review', views.createReview, name="createReview"),
    path('<post_id>/review/<review_id>', views.reviewDetail, name="readUpdateDelete"),
]