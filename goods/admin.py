from django.contrib import admin

# Register your models here.
from goods.models import *


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro', 'price', 'unit', 'click', 'type']


admin.site.register(GoodsType)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
