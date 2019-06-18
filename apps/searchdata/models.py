from django.db import models
from datetime import datetime

# Create your models here.
class SearchData(models.Model):
    webproject = models.CharField(max_length=100, default="", verbose_name=u"web后台项目")
    testpage = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    isclicklastpage = models.BooleanField(default=False,verbose_name=u"是否点击最后一页页码")
    selectxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"筛选字段选项Xpath路径")
    selectoptiontextxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"筛选字段选项内容Xpath路径")
    selectinputxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"筛选字段选项对应输入框的Xpath路径")
    selectinputselectonexpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"筛选字段选项对应输入框输入内容后下拉列表第一项的Xpath路径")
    selectinputtext = models.CharField(max_length=500, default="",null=True, blank=True, verbose_name=u"筛选字段选项对应输入框的输入内容")
    isfind = models.BooleanField(default=False,verbose_name=u"筛选结果是否有相应内容")
    colnum = models.CharField(max_length=100, default="0",verbose_name=u"搜索结果表格的列数")
    checktext = models.CharField(max_length=100, default="Corresponding data not queried!", verbose_name=u"搜索结果表格的列数对应的预期文本内容")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加页面时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"检索测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

