from django.db import models
from datetime import datetime

# Create your models here.
class LoginData(models.Model):
    webproject = models.CharField(max_length=100, default="", verbose_name=u"web后台项目")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    accountinput = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"账号输入内容")
    passwordinput = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"密码输入内容")
    vercodeinput = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"验证码输入内容")
    assertaccounttiptext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"账号提示内容")
    assertpasswordtiptext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"密码提示内容")
    assertvercodetiptext = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"验证码提示内容")
    assertlogintiptext = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"点击登录提示内容")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加页面时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"登录测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

