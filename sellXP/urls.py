from django.urls import path
from . import views

urlpatterns = [
    path('sellXP/', views.getPosts, name="getPosts"),
    path('sellXP/create', views.createPosts, name="createPosts"),
    path('sellXP/update/<post_id>', views.updatePosts, name="updatePosts"),
    path('sellXP/delete/<int:post_id>', views.deletePost, name="deletePost"),
    path('<sellXP_id>/reviews', views.getReviews, name="getReviews"),
    path('<sellXP_id>/review', views.createReview, name="createReview"),
    path('<sellXP_id>/review/<sell_review_id>', views.reviewDetail, name="readUpdateDelete"),
]