from django.contrib import admin
from django.urls import URLPattern, path
from yourXP import views

URLPatterns = [
    path('/admin', admin.site.urls),
    path('detail/<int:buy_id', views.detail, name = "detail"),
    path('create', views.create, name="create"),
  #  path('update/<int: buy_id>', views.update, name = "update"),
]

