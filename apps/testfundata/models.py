from datetime import datetime
from django.db import models

from pageelement.models import ModulePage,PageEle

# Create your models here.
class TestSearch(models.Model):
    """
    搜索测试
    """
    is_cookie = models.BooleanField(default=True)
    modulepage = models.ForeignKey(ModulePage,default="", verbose_name=u"模块页面", on_delete=models.PROTECT)
    select_option_xpath = models.ForeignKey(PageEle,default="", verbose_name="select_option_xpath",null=True, blank=True, on_delete=models.PROTECT,related_name="sox")
    select_option_text = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"select_option_text")
    select_input_xpath = models.ForeignKey(PageEle,default="", verbose_name="select_input_xpath",null=True, blank=True, on_delete=models.PROTECT,related_name="six")
    select_input_text = models.CharField(max_length=1000, default="", null=True, blank=True,verbose_name=u"select_input_text")
    search_button_xpath = models.ForeignKey(PageEle, verbose_name="search_button_xpath", on_delete=models.PROTECT)
    search_table_result_xpath =  models.ForeignKey(PageEle, default="",verbose_name="search_table_result_xpath",on_delete=models.PROTECT,related_name="strx")
    colnum = models.CharField(max_length=100, default="0", verbose_name=u"colnum")
    check_text = models.CharField(max_length=1000, default="", verbose_name=u"check_text")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间


    class Meta:
        verbose_name = u"搜索测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return str(self.add_time)

    # def get_module_nums(self):
    #     #获取项目的模块数
    #     return self.projectmodule_set.all().count()
    #     # return self.projectmodule_set.all().filter(testproject__web_project =self.web_project).count()
    #
    # get_module_nums.short_description = "模块数"

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='http://127.0.0.1:8000/testfun/testsearchcopy/{}/'>复制新加</a>".format(self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字
