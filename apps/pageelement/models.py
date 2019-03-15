from datetime import datetime
from django.db import models
from django.db.models import Q   #导入Q，筛选作为或与用


# Create your models here.
class TestProject(models.Model):
    """
    测试项目
    """
    web_project = models.CharField(max_length=100, default="", verbose_name=u"web项目",unique=True)   #unique=True,表示唯一
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加项目时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间


    class Meta:
        verbose_name = u"测试项目"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.web_project

    # def get_module_nums(self):
    #     #获取项目的模块数
    #     return self.projectmodule_set.all().count()
    #     # return self.projectmodule_set.all().filter(testproject__web_project =self.web_project).count()
    #
    # get_module_nums.short_description = "模块数"

    # def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='http://127.0.0.1:8000/pageele/modulepagecopy/{}/'>复制新加</a>".format(self.id))
    #     # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)
    #
    # go_to.short_description = u"复制新加"   #为go_to函数名个名字


# Create your models here.
class ProjectModule(models.Model):
    """
    项目模块
    """
    # testproject = models.ForeignKey(TestProject, verbose_name=u"测试项目", on_delete=models.PROTECT)
    web_module = models.CharField(max_length=100, default="", verbose_name=u"项目模块",unique=True)   #unique=True,表示唯一
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加模块时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"项目模块"
        verbose_name_plural = verbose_name
        # unique_together = ("testproject", "web_module")  # unique_together中设置的字段作为联合唯一索引。不会出现这里设置的字段联合起来会有两条数据的情况
        # 此处设置"testproject"和"web_module"组成联合唯一，如果出现重复，数据库会进行处理，抛出异常
        # 设置完成后，一定要makemigrations和migrate,但设置之前要先将该表清空，因为如果表里有重复数据会migrate失败

    def __str__(self):
        return self.web_module

    # def get_page_nums(self):
    #     #获取模块的页面数
    #     # return self.modulepage_set.all().count()
    #     return self.modulepage_set.all().filter(testproject_id=self.testproject_id).count()
    # get_page_nums.short_description = "页面数"

    # def go_to(self):  # 定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='http://127.0.0.1:8000/pageele/modulepagecopy/{}/'>复制新加</a>".format(self.id))
    #     # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)
    #
    # go_to.short_description = u"复制新加"  # 为go_to函数名个名字

# Create your models here.
class ModulePage(models.Model):
    """
    模块页面
    """
    testproject = models.ForeignKey(TestProject, verbose_name=u"测试项目", on_delete=models.PROTECT)
    projectmodule = models.ForeignKey(ProjectModule, verbose_name=u"项目模块", on_delete=models.PROTECT)
    ele_page = models.CharField(max_length=100, default="", verbose_name=u"元素页面")
    ele_page_url = models.CharField(max_length=1000, default="", null=True, blank=True,  verbose_name=u"元素页面URL")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加页面时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"模块页面"
        verbose_name_plural=verbose_name
        unique_together = ("testproject", "projectmodule","ele_page")  # unique_together中设置的字段作为联合唯一索引。不会出现这里设置的字段联合起来会有两条数据的情况
        # 此处设置"testproject","projectmodule"和"ele_page"组成联合唯一，如果出现重复，数据库会进行处理，抛出异常
        # 设置完成后，一定要makemigrations和migrate,但设置之前要先将该表清空，因为如果表里有重复数据会migrate失败


    def __str__(self):
        return "[%s__%s_%s]" %(self.testproject.web_project,self.projectmodule.web_module,self.ele_page)

    # def get_page_ele_nums(self):
    #     #获取页面的元素数
    #     return self.pageele_set.all().count()
    #     # return self.pageele_set.all().filter(Q(testproject__web_project =self.testproject__web_project)&Q(projectmodule__web_module =self.projectmodule__web_module)).count()
    #
    # get_page_ele_nums.short_description = "页面元素数"

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='http://127.0.0.1:8000/pageele/modulepagecopy/{}/'>复制新加</a>".format(self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字


# Create your models here.
class PageEle(models.Model):
    """
    页面元素
    """
    # testproject = models.ForeignKey(TestProject, verbose_name=u"测试项目", on_delete=models.PROTECT)
    # projectmodule = models.ForeignKey(ProjectModule, verbose_name=u"项目模块", on_delete=models.PROTECT)
    modulepage = models.ForeignKey(ModulePage, verbose_name=u"模块页面", on_delete=models.PROTECT)
    ele_name = models.CharField(max_length=100, default="", verbose_name=u"元素名字")
    ele_xpath = models.CharField(max_length=1000, default="", verbose_name=u"元素xpath路径")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"页面元素"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "【%s-%s】"%(self.modulepage,self.ele_name)

    # def get_ele_test_data_type_nums(self):
    #     #获取页面的元素类型数
    #     return self.eletestdatatype_set.all().count()
    #
    # get_ele_test_data_type_nums.short_description = "测试数据类型数"

    # def get_ele_test_data_nums(self):
    #     #获取页面的元素类型数
    #     return self.eletestdata_set.all().filter(pageele_id=self.id).count()
    #
    # get_ele_test_data_nums.short_description = "测试数据个数"

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='http://127.0.0.1:8000/pageele/pageelecopy/{}/'>复制新加</a>".format(self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字


# Create your models here.
class EleTestDataType(models.Model):
    """
    元素测试数据类型
    """
    # testproject = models.ForeignKey(TestProject, verbose_name=u"测试项目", on_delete=models.PROTECT)
    # projectmodule = models.ForeignKey(ProjectModule, verbose_name=u"项目模块", on_delete=models.PROTECT)
    # modulepage = models.ForeignKey(ModulePage, verbose_name=u"模块页面", on_delete=models.PROTECT)
    # pageele = models.ForeignKey(PageEle, verbose_name="页面元素", on_delete=models.PROTECT)
    test_data_type = models.CharField(max_length=100, default="", verbose_name=u"测试数据类型",unique=True)   #unique=True,表示唯一
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"元素测试数据类型"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.test_data_type

    # def get_ele_test_data_nums(self):
    #     #获取页面的元素类型数
    #     return self.eletestdata_set.all().count()
    #
    # get_ele_test_data_nums.short_description = "测试数据个数"


# Create your models here.
class EleTestData(models.Model):
    """
    元素测试数据
    """
    # testproject = models.ForeignKey(TestProject, verbose_name=u"测试项目", on_delete=models.PROTECT)
    # projectmodule = models.ForeignKey(ProjectModule, verbose_name=u"项目模块", on_delete=models.PROTECT)
    # modulepage = models.ForeignKey(ModulePage, verbose_name=u"模块页面", on_delete=models.PROTECT)
    pageele = models.ForeignKey(PageEle, verbose_name="页面元素", on_delete=models.PROTECT)
    eletestdatatype = models.ForeignKey(EleTestDataType, verbose_name=u"元素测试数据类型", on_delete=models.PROTECT)
    test_data = models.CharField(max_length=1000, default="", verbose_name=u"元素测试数据")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"元素测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.test_data


    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='http://127.0.0.1:8000/pageele/eletestdatacopy/{}/'>复制新加</a>".format(self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字




