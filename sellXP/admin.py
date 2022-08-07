from django.contrib import admin
from .models import SellXP, SellXP_tag
from .models import Sell_review

# Register your models here.
admin.site.register(SellXP)
admin.site.register(SellXP_tag)
admin.site.register(Sell_review)