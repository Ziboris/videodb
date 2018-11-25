from django.db import models
from jsonfield import JSONField
# Create your models here.


class CVE_Case(models.Model):
    case_id=models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="video_id")
    name=models.CharField(max_length=200) #varchar
    # url = models.FileField(upload_to='videos', default="")

    jumpArg=models.IntegerField(default=0) #组接参数1，跳剪，是、否  0.1
    speedArg=models.IntegerField(default=0) #组接参数2，主体运动状态，运动/平稳 0.1
    positionArg=models.IntegerField(default=0) #组接参数3，主体位置，一致/不一致 0.1
    cramArg=models.IntegerField(default=0) #组接参数4，镜头运动状态，运动/平稳 0.1
    colorArg=models.IntegerField(default=0) #组接参数5，色调，一致/对比 0.1



class CVE_Shot(models.Model):
    shot_id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="shot_id")
    case_id = models.IntegerField()
    start=models.IntegerField(default=0) #镜头起始帧 int
    end=models.IntegerField(default=0) #镜头结束帧 int
    during=models.IntegerField(default=0) #镜头属性0，时长 int

    speed=JSONField() #镜头属性1，主体运动状态 [x,y]
    position=JSONField() #镜头属性2，主体位置 [x,y]
    craMotion=JSONField() #镜头属性3，镜头运动状态 [x,y]
    color=JSONField() #镜头属性4，色调 [x,y]
    shotSize=models.IntegerField(default=0) #镜头属性5，景别 0-3

class CVE_Case_Tags(models.Model):
    case_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False) #id
    container=models.IntegerField(default=0) #视频载体: 手机 电视 （大屏）
    scenes=models.IntegerField(default=0) #业务场景: 商品上新 促销 品牌宣传
    productCategory=models.IntegerField(default=0) #产品分类: 女装 男装 （童装 服装配饰 宠物用品 配饰）
    style=models.IntegerField(default=0) #风格-需要支持模糊搜索（汉字）



    # product_type=models.IntegerField() #产品类型 0.1.2
    # busi_orientation=models.IntegerField() #业务导向 0.1.2
    # product_style=models.IntegerField() #产品风格 0.1.2
    # media=models.IntegerField() #传播载体 0.1.2
    # year=models.IntegerField() #年份 0.1.2.3.4.5.6.7.8.9.10
    # consumer=models.IntegerField() #消费者 0.1.2