from django.urls import path
from .import views

urlpatterns = [
    path('', views.getUsers, name="getUsers"),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),    
    path('logout', views.logout_view, name='logout'),
    path('<user_id>', views.userDetail, name="readUpdateDelete"),
    path('<user_id>/point', views.pointDetail, name="pointDetail"),
]