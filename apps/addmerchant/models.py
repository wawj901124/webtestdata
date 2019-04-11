from django.db import models
from datetime import datetime

# Create your models here.
class AddMerchant(models.Model):
    webproject = models.CharField(max_length=100, default="", verbose_name=u"web后台项目")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    brandnameinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入Brand name的内容")
    emailinputtext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入Email的内容")
    contactnumberinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Contact number的内容")
    merchanttypeselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"Merchant type选项内容Xpath路径")
    categoryselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"Category选项内容Xpath路径")
    criteriaselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"Criteria选项内容Xpath路径")
    siupinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入SIUP的内容")
    provinceselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"Province选项内容Xpath路径")
    cityselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"City选项内容Xpath路径")
    districtinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入District的内容")
    villageinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Village的内容")
    postcodeinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Postcode的内容")
    addressinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Address的内容")
    photosiupimagefilepath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"添加Photo SIUP图片的路径")
    photonpwpcompanyimagefilepath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"添加Photo NPWP Company图片的路径")
    phototdpimagefilepath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"添加Photo TDP图片的路径")
    nameinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Name的内容")
    npwpinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入NPWP的内容")
    typeidselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"Type ID选项内容Xpath路径")
    identitynumberinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Identity number的内容")
    address2inputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Address的内容")
    nationalityselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"Nationality选项内容Xpath路径")
    phoneinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Phone的内容")
    email2inputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Email的内容")
    photofullfacebustimagefilepath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"添加Photo Full-faceBust图片的路径")
    locationphotoimagefilepath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"添加Location Photo图片的路径")
    photoofthecashiersdeskimagefilepath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"添加Photo of the cashiers desk图片的路径")
    otherphotoimagefilepath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"添加Other Photo图片的路径")
    bankselectoptionxpath = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"Bank选项内容Xpath路径")
    accountnameinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Account name的内容")
    accountnumberinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入Account number的内容")
    qrindoaccountinputtext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"输入QRindo account的内容")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"添加商户测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

