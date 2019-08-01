from django.db import models
from datetime import datetime

# Create your models here.
class MeminfoTestCase(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    currentpagetext = models.CharField(max_length=100, default="", verbose_name=u"输入当前页面标识元素text",help_text=u"当前页面标识元素text")
    currrentfindstyle = models.CharField(max_length=100, default="", verbose_name=u"要点击元素查找风格",help_text=u"要点击元素查找风格，例如resourceId、text")
    currentstyleparame = models.CharField(max_length=1000, default="", verbose_name=u"要点击元素查找风格的确切值",help_text=u"要点击元素查找风格的确切值")
    nextpagetext = models.CharField(max_length=100, default="", verbose_name=u"输入下一个页面标识元素text",help_text=u"下一个页面标识元素text")
    forcount = models.IntegerField(verbose_name="用例循环次数",help_text=u"用例循环次数")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"内存测试用例"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle


class MeminfoTestResult(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    teststarttime = models.CharField(max_length=100, default="", verbose_name=u"开始运行时间")
    forcount = models.CharField(max_length=100, default="", verbose_name=u"第几次循环")
    currentpagememinfo = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面内存",help_text=u"当前页面内存（单位：KB）")
    currentpageaftertenmeminfo = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"当前页面静置10秒后内存",
                                          help_text=u"当前页面静置10秒后内存（单位：KB）")
    clicknextpagememinfo = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"点击进入下一个页面内存",
                                          help_text=u"点击进入下一个页面内存（单位：KB）")
    nextaftertenmeminfo = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"静置10秒后内存",
                                          help_text=u"静置10秒后内存（单位：KB）")
    nextaftertenmeminfotwo = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"再次静置10秒后内存",
                                          help_text=u"再次静置10秒后内存（单位：KB）")
    clickbackmeminfo = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"点击返回后内存",
                                          help_text=u"点击返回后内存（单位：KB）")
    backaftertenmeminfo = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"静置10秒后内存",
                                          help_text=u"静置10秒后内存（单位：KB）")
    backaftertenmeminfotwo = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"再次静置10秒后内存",
                                          help_text=u"再次静置10秒后内存（单位：KB）")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"内存测试结果统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

