from django.urls import path
from .import views

urlpatterns = [
    path('buys/hits', views.hitsGetBuyXP, name="getBuyXP"),
    path('buys/views', views.viewsGetBuyXP, name="getBuyXP"),
    path('buys/<str:search_keyword>', views.searchBuyXP, name='searchBuyXP'),
    path('buys/detail/<buyXP_id>', views.detailBuyXP, name="detailBuyXP"),
    path('buy', views.createBuyXP, name="createBuyXP"),
    path('buys/update/<buyXP_id>', views.updateBuyXP, name="updateBuyXP"),
    path('buys/delete/<int:buyXP_id>', views.deleteBuyXP, name="deleteBuyXP"),
    path('tag/<buyXPtag_id>', views.getBuyXP_tag, name="getBuyXP_tag"),
    path('tag_create/<buyXPtag_id>', views.createBuyXP_tag, name="createBuyXP_tag"),
    path('tag_update/<buyXPtag_id>', views.buyXP_tag_detail, name="buyXP_tag_detail"),
]