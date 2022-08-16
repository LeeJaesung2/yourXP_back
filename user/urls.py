from django.urls import path
from .import views

urlpatterns = [
    path('', views.getUsers, name="getUsers"),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),    
    path('logout', views.logout_view, name='logout'),
    path('<username>', views.userDetail, name="readUpdateDelete"),
    path('<username>/point', views.pointDetail, name="pointDetail"),
]