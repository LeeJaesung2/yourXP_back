from django.urls import path
from .import views

urlpatterns = [
    path('all', views.getUsers, name="getUsers"),
    path('', views.createUser, name="createUser"),
    path('<user_id>', views.userDetail, name="readUpdateDelete"),
]