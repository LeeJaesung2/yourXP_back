from django.contrib import admin
from .models import SellXP, SellXP_tag, Sell_image, Sell_review

# Register your models here.
admin.site.register(SellXP)
admin.site.register(SellXP_tag)
admin.site.register(Sell_review)
admin.site.register(Sell_image)