from django.db import models
from datetime import datetime

# Create your models here.
class InputTipData(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    isinput = models.BooleanField(default=False,verbose_name=u"是否输入内容")
    inputxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"输入框Xpath路径")
    inputtext = models.CharField(max_length=1500, default="",null=True, blank=True, verbose_name=u"输入框的输入内容")
    inputtipxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"输入框下Tip提示信息Xpath路径")
    inputtiptext = models.CharField(max_length=500, default="",null=True, blank=True, verbose_name=u"输入框下Tip提示信息内容")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"输入框提示测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

