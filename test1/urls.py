"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from BookInfo import views
from django.conf.urls import url
from django.conf.urls import url,include

# 项目的url配置文件
#path不能是调自定义的模块,url 不能调用 第三方的界面吗
urlpatterns = [
    path('admin/', admin.site.urls), #配置项
    path('index/',views.index),
    path('books/', views.show_books),#显示图书信息
    re_path('books/(\d+)$', views.detail)#显示图书信息
    # url(r'^$', include('BookInfo.urls')),#包含BookInfo的urls文件
]
