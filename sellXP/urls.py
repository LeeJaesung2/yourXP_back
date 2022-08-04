from django.urls import path
from . import views

urlpatterns = [
    path('sellXP/', views.getPosts, name="getPosts"),
    path('sellXP/create', views.createPosts, name="createPosts"),
    path('sellXP/update/<post_id>', views.updatePosts, name="updatePosts"),
    path('sellXP/delete/<int:post_id>', views.deletePost, name="deletePost"),
]