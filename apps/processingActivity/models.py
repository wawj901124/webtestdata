from django.db import models
from datetime import datetime

# Create your models here.
class ProcessActivity(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    zjysinputtext = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"输入增加预算的内容")
    ffzt = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入发放状态的单选的内容",help_text=u"1表示开启，否则为关闭")
    zjkcinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入增加库存的内容")
    isqcancel = models.BooleanField(default=False, verbose_name=u"是否点击券页取消按钮")
    iscancel = models.BooleanField(default=False, verbose_name=u"是否点击取消按钮")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"添加进行中的活动的测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

