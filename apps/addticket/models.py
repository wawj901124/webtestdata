from django.db import models
from datetime import datetime

# Create your models here.
class AddTicket(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    ffzt = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入发放状态的单选的内容",help_text=u"1表示开启，否则为关闭")
    kcslinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入库存数量的内容")
    qyxq = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入券有效期的选项的内容",help_text=u"1表示相对时间，否则为绝对时间")
    xdsjtsinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入券有效期选择相对时间时相对天数的内容")

    yxcbcdf = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入营销成本承担方的单选内容",help_text=u"1表示平台，否则为商户")
    yhqmcinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入优惠券名称的内容")
    yhlx = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入优惠类型的选项的内容",help_text=u"1表示代金券")
    yhms = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入优惠模式的选项的内容",help_text=u"1表示固定金额，否则为随机金额")
    gdjemzinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入固定金额的面值的内容")
    sjjemzmiminputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入随机金额的面值的最小值的内容")
    sjjemzmimaxinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入随机金额的面值的最大值的内容")
    zdxfinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入最低消费的内容")
    sypt = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入使用平台的复选的内容",help_text=u"0表示两个都点选，1表示点选QRindo，为2表示点选PaySDK")
    syfw = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入使用范围的选项的内容",help_text=u"1表示不限，为2表示指定行业，为3表示指定商户")
    zdhyoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"输入指定行业的选项的xpath的内容")
    zdshinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入指定商户的商户名称或ID的内容")
    isplsh = models.BooleanField(default=False,verbose_name=u"是否使用批量导入商户功能")
    plfilepath = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入导入批量商户的文件的路径")
    kfyqthddj = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入可否与其他活动叠加的单选的内容",help_text=u"1表示不可以叠加使用，为2表示可以叠加使用")
    sfzctq = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入是否支持退券的单选的内容",help_text=u"1表示可退，为2表示不可退")
    iscancel = models.BooleanField(default=False, verbose_name=u"是否点击取消按钮")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"添加代金券测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

