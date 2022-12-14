from django.urls import path, include
from . import views
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf import settings
from sellXP.views import sellXPViewSet

router = DefaultRouter()
router.register(r'create', views.sellXPViewSet)


urlpatterns = [
    path('views', views.viewsGetSellXPs, name="viewsGetSellXPs"), 
    path('viewsrank', views.viewsGetSellXPsRank, name="viewsGetSellXPsRank"), 
    # path('recommends', views.recommendsGetSellXPs, name="recommendGetSellXPs"),    
    path("", include(router.urls)), #127.0.0.1/SellXP/create
    #path('create', views.createSellXP, name="createSellXP"),
    path('<sellXP_id>', views.getSellXP, name="getSellXP"),
    path('update/<sellxp_id>', views.updateSellXP, name="updateSellXP"),
    path('delete/<int:sellxp_id>', views.deleteSellXP, name="deleteSellXP"),
    path('<sellXP_id>/reviews', views.getReviews, name="getReviews"),
    path('<sellXP_id>/review', views.createReview, name="createReview"),
    path('<sellXP_id>/review/<sell_review_id>', views.reviewDetail, name="readUpdateDelete"),
    path('like/<int:sellxp_id>', views.sellXP_like, name="sellXP_like"),
    path('search/<str:sellName>', views.searchSellXP, name="searchSellXP"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
