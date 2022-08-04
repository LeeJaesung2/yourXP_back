from django.urls import path
from .import views

urlpatterns = [
    path('users', views.getUsers, name="getUsers"),
    path('user', views.createUser, name="createUser"),
    path('user/<user_id>', views.userDetail, name="readUpdateDelete"),
]