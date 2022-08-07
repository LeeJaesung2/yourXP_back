from django.urls import path
from .import views

urlpatterns = [
    path('', views.getUsers, name='getUsers'),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('login1', views.login_view1, name='login1'),
    path('login2', views.login_view2, name='login2'),
    path('login3', views.login, name='login3'),
    path('logout', views.logout_view, name='logout'),
    path('<user_id>', views.userDetail, name="readUpdateDelete"),
]