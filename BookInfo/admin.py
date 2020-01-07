from django.contrib import admin
from BookInfo.models import BookInfo, HeroInfo
# 后台管理相关文件
# Register your models here.
# 自定义类 模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """"图书模型管理类"""
    list_display = ["id", "btitel","bpub_data"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "hcomment"]


# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)