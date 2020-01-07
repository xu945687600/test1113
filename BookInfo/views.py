from django.shortcuts import render
from django.http import HttpResponse
import datetime
from BookInfo.models import BookInfo

# Create your views here.
# 1.定义视图函数HttepRequest
#2.进行url的配置，简历url地址跟视图的对应
# http://127.0.0.1:8000/index



li = [1, 2, 3 ,4]
dic = {'add':"江西", 'tel':87777, 'sex':"girl"}
def index(request):
    """"使用模板文件"""
    return render(request, 'BookInfo/index.html', context={
        "li":li,
        'dic':dic,
        'time':datetime.datetime.now()
    })

# 使用模板文件
# 1加载模板文件
# temp = loader.get_template('BookInfo/index.html')
#
# # 第一模板上下文；给模板文件传递数据R
# context = RequestContext(request, {})

def show_books(request):
    """"显示图书信息"""
# 1.通过M查找图书表中数据
    books = BookInfo.objects.all()
    return render(request, 'BookInfo/show_books.html', {'books':books})

def detail(request, bid):
    """"查询图书关联的图书信息"""
    # 1.根据bid查询图书
    book = BookInfo.objects.get(id = bid)
    # 2.查询跟book关联的英雄信息
    heros = book.heroinfo_set.all()
    # 3.使用模板
    return render(request, 'BookInfo/detail.html',{'books':book, 'heros':heros} )