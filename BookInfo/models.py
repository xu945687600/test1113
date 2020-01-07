from django.db import models

# 设计和表对应的类，模型类
# Create your models here
#一类
class BookInfo(models.Model):
    """"图书模型类"""
    # 图书标题，CharField表示是一个字符串，max_length表示长度
    btitel = models.CharField(max_length=20)
    # 出版日期，DateField是一个日期类型
    bpub_data = models.DateField()
    def __str__(self): #返回书名
        return self.btitel


# 英雄人物类
# 英雄名字  hname
# 英雄年龄 hage
# 性别  hgender
# 备注 hcomment
# 关系属性 book建立图书类跟人物类一对多的关系
# 多类
class HeroInfo(models.Model):

    hname = models.CharField(max_length=20) #英雄名称
    # 性别BooleanField是bool类型，default指定默认值 false代表男
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    # 关系属性类，建立图书类跟英雄类之间的一对多的关系
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self): #返回英雄名
        return self.hname
