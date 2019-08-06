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
    currentpagepsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面Pss Total内存",help_text=u"当前页面Pss Total内存（单位：KB）")
    currentpageheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面Heap Size内存",help_text=u"当前页面Heap Size内存（单位：KB）")
    currentpageheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面Heap Alloc内存",help_text=u"当前页面Heap Alloc内存（单位：KB）")
    currentpageheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面Heap Free内存",help_text=u"当前页面Heap Free内存（单位：KB）")
    currentpageobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面Objects Viewss数",help_text=u"当前页面Objects Viewss数（单位：个）")
    currentpageobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面Objects Activities数",help_text=u"当前页面Objects Activities数（单位：个）")

    currentpageaftertenpsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面静置10秒后Pss Total内存",help_text=u"当前页面静置10秒后Pss Total内存（单位：KB）")
    currentpageaftertenheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面静置10秒后Heap Size内存",help_text=u"当前页面静置10秒后Heap Size内存（单位：KB）")
    currentpageaftertenheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面静置10秒后Heap Alloc内存",help_text=u"当前页面静置10秒后Heap Alloc内存（单位：KB）")
    currentpageaftertenheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面静置10秒后Heap Free内存",help_text=u"当前页面静置10秒后Heap Free内存（单位：KB）")
    currentpageaftertenobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面静置10秒后Objects Viewss数",help_text=u"当前页面静置10秒后Objects Viewss数（单位：个）")
    currentpageaftertenobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"当前页面静置10秒后Objects Activities数",help_text=u"当前页面静置10秒后Objects Activities数（单位：个）")

    clicknextpagepsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击进入下一个页面Pss Total内存",help_text=u"点击进入下一个页面Pss Total内存（单位：KB）")
    clicknextpageheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击进入下一个页面Heap Size内存",help_text=u"点击进入下一个页面Heap Size内存（单位：KB）")
    clicknextpageheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击进入下一个页面Heap Alloc内存",help_text=u"点击进入下一个页面Heap Alloc内存（单位：KB）")
    clicknextpageheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击进入下一个页面Heap Free内存",help_text=u"点击进入下一个页面Heap Free内存（单位：KB）")
    clicknextpageobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击进入下一个页面Objects Viewss数",help_text=u"点击进入下一个页面Objects Viewss数（单位：个）")
    clicknextpageobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击进入下一个页面Objects Activities数",help_text=u"点击进入下一个页面Objects Activities数（单位：个）")


    nextaftertenpsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页静置10秒后Pss Total内存",help_text=u"进入页静置10秒后Pss Total内存（单位：KB）")
    nextaftertenheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页静置10秒后Heap Size内存",help_text=u"进入页静置10秒后Heap Size内存（单位：KB）")
    nextaftertenheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页静置10秒后Heap Alloc内存",help_text=u"进入页静置10秒后Heap Alloc内存（单位：KB）")
    nextaftertenheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页静置10秒后Heap Free内存",help_text=u"进入页静置10秒后Heap Free内存（单位：KB）")
    nextaftertenobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页静置10秒后Objects Viewss数",help_text=u"进入页静置10秒后Objects Viewss数（单位：个）")
    nextaftertenobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页静置10秒后Objects Activities数",help_text=u"进入页静置10秒后Objects Activities数（单位：个）")

    nextaftertentwopsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页再次静置10秒后Pss Total内存",help_text=u"进入页再次静置10秒后Pss Total内存（单位：KB）")
    nextaftertentwoheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页再次静置10秒后Heap Size内存",help_text=u"进入页再次静置10秒后Heap Size内存（单位：KB）")
    nextaftertentwoheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页再次静置10秒后Heap Alloc内存",help_text=u"进入页再次静置10秒后Heap Alloc内存（单位：KB）")
    nextaftertentwoheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页再次静置10秒后Heap Free内存",help_text=u"进入页再次静置10秒后Heap Free内存（单位：KB）")
    nextaftertentwoobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页再次静置10秒后Objects Viewss数",help_text=u"进入页再次静置10秒后Objects Viewss数（单位：个）")
    nextaftertentwoobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"进入页再次静置10秒后Objects Activities数",help_text=u"进入页再次静置10秒后Objects Activities数（单位：个）")

    clickbackpsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击返回后Pss Total内存",help_text=u"点击返回后Pss Total内存（单位：KB）")
    clickbackheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击返回后Heap Size内存",help_text=u"点击返回后Heap Size内存（单位：KB）")
    clickbackheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击返回后Heap Alloc内存",help_text=u"点击返回后Heap Alloc内存（单位：KB）")
    clickbackheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击返回后Heap Free内存",help_text=u"点击返回后Heap Free内存（单位：KB）")
    clickbackobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击返回后Objects Viewss数",help_text=u"点击返回后Objects Viewss数（单位：个）")
    clickbackobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"点击返回后Objects Activities数",help_text=u"点击返回后Objects Activities数（单位：个）")

    backaftertenpsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页静置10秒后Pss Total内存",help_text=u"返回页静置10秒后Pss Total内存（单位：KB）")
    backaftertenheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页静置10秒后Heap Size内存",help_text=u"返回页静置10秒后Heap Size内存（单位：KB）")
    backaftertenheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页静置10秒后Heap Alloc内存",help_text=u"返回页静置10秒后Heap Alloc内存（单位：KB）")
    backaftertenheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页静置10秒后Heap Free内存",help_text=u"返回页静置10秒后Heap Free内存（单位：KB）")
    backaftertenobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页静置10秒后Objects Viewss数",help_text=u"返回页静置10秒后Objects Viewss数（单位：个）")
    backaftertenobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页静置10秒后Objects Activities数",help_text=u"返回页静置10秒后Objects Activities数（单位：个）")

    backaftertentwopsstotal = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页再次静置10秒后Pss Total内存",help_text=u"返回页再次静置10秒后Pss Total内存（单位：KB）")
    backaftertentwoheapsize = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页再次静置10秒后Heap Size内存",help_text=u"返回页再次静置10秒后Heap Size内存（单位：KB）")
    backaftertentwoheapalloc = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页再次静置10秒后Heap Alloc内存",help_text=u"返回页再次静置10秒后Heap Alloc内存（单位：KB）")
    backaftertentwoheapfree = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页再次静置10秒后Heap Free内存",help_text=u"返回页再次静置10秒后Heap Free内存（单位：KB）")
    backaftertentwoobjectsviews = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页再次静置10秒后Objects Viewss数",help_text=u"返回页再次静置10秒后Objects Viewss数（单位：个）")
    backaftertentwoobjectsactivities = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"返回页再次静置10秒后Objects Activities数",help_text=u"返回页再次静置10秒后Objects Activities数（单位：个）")

    test_phone_name = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试手机ID")
    test_app_packagename = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试应用包名")
    test_app_version = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试应用版本号")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"内存测试结果统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

