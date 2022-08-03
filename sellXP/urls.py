from django.urls import path
from .import views

urlpatterns = [
    path('reviews', views.getReviews, name="getReviews"),
    path('review', views.createReview, name="createReview"),
    path('review/<review_id>', views.getReviewById, name="getReviewById"),
    path('review/<review_id>', views.updateReview, name="updateReview"),
    path('review/<review_id>', views.deleteReview, name="deleteReview"),
]