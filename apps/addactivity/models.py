from django.db import models
from datetime import datetime

# Create your models here.
class AddActivity(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")

    hdmcinputtext= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入活动名称的内容")
    hdysinputtext= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入活动预算的内容")
    tfqdyj= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入投放渠道一级的选项的内容",help_text=u"投放渠道一级为1表示内部渠道，为2表示外部渠道")
    tfqdej= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入投放渠道二级的复选的内容",help_text=u"投放渠道二级为0表示全选，为1，2，等表示选一项和选多项组合，程序中只有全选和选择一项的情况")
    hdbztextareainputtext= models.CharField(max_length=2000, default="",null=True, blank=True, verbose_name=u"输入活动备注的内容")
    rwlx= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入任务类型的选项的内容",help_text=u"任务类型为1表示注册，为2表示交易类型")
    tjrwxz= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入点击添加任务弹窗中的选项的内容",help_text=u"1表示选择交易类型，2表示选择支付方式，3表示选择用户活动参与次数")
    jyjylx= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入交易类型的复选的内容",help_text=u"0表示选择所有项，1表示只选择消费，2表示只选择充值，3表示只选择转账")
    jyzffs= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入支付方式的复选的内容",help_text=u"0表示选择所有项，1表示只选择钱包余额，2表示只选择银行卡")
    jymgyhzdcycsinputtext= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入每个用户最多参与次数的内容")
    jymgyhmrcycsinputtext= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入每个用户每日参与次数的内容")
    jllx= models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"输入选择奖励类型选项的内容",help_text=u"1表示固定奖励")
    iscancel= models.BooleanField(default=False, verbose_name=u"是否点击取消按钮")

    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"添加活动测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle

