import unittest

from webtestdata.settings import WEB_URL_TITLE,AGENT_LOGIN_ACCOUNT,AGENT_LOGIN_PASSWORD


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson
from TestCaseFunction.util.gettimestr import GetTimeStr

from TestCaseFunction.autotest.config.page.manager.loginPage import LoginPage   #导入登录页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityCreatePage import ActivityCreatePage   #导入创建活动页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.ticketCreatePage import TicketCreatePage   #导入创建优惠券页

class TestCreateActivityClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        # from base.getcookie import GetCookie
        # outjsonfile = "../../../cookiejson/cookiemanager.json"
        # outloginurl = LoginPage().pageurl
        # outloginaccountxpath = LoginPage().account
        # outloginaccounttext = "81122336666"
        # outloginppasswordxpath = LoginPage().password
        # outloginpasswordtext = "abc123456"
        # outloginbuttonxpath = LoginPage().loginbutton
        #
        # getcookie = GetCookie(outjsonfile=outjsonfile, outloginurl=outloginurl,
        #                       outloginaccountxpath=outloginaccountxpath,
        #                       outloginaccounttext=outloginaccounttext, outloginppasswordxpath=outloginppasswordxpath,
        #                       outloginpasswordtext=outloginpasswordtext,
        #                       outloginbuttonxpath=outloginbuttonxpath)  # 实例化
        # getcookie.writerCookieToJson()

        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        # self.jsonfile = '../../../cookiejson/cookieagent.json'
        # self.operationjson = OperationJson(file_path=self.jsonfile)   #实例化
        # self.cookie = self.operationjson.get_all_data()
        # print("self.cookie:%s" % self.cookie)
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = LoginPage().pageurl
        self.activeweb.getUrl(self.loginurl)  # 打开网址
        self.activeweb.findElementByXpathAndInput(LoginPage().account,AGENT_LOGIN_ACCOUNT)
        self.activeweb.findElementByXpathAndInput(LoginPage().password,AGENT_LOGIN_PASSWORD)
        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = ActivityCreatePage()
        self.testpageurl =self.testpage.pageurl   #测试页面url
        self.testpagehdmcinput = self.testpage.hdmc_input       # ---基础信息---#   活动名称输入框路劲
        self.testpagehdsjstarttime = self.testpage.hdsj_starttime # ---基础信息---#   活动时间开始时间输入框路径
        self.testpagehdsjendtime = self.testpage.hdsj_endtime  # ---基础信息---#   活动时间结束时间输入框路径
        self.testpagehdysinput  = self.testpage.hdys_input   # ---基础信息---#   活动预算输入框路径
        self.testpagetfqdselect = self.testpage.tfqd_select   # ---基础信息---#  投放渠道下拉框路径
        self.testpagehdbztextarea = self.testpage.hdbz_textarea   # ---基础信息---#  活动备注多行输入框路径
        self.testpagerwlxselect = self.testpage.rwlx_select       # ---活动任务规则---# 任务类型下拉框路径
        self.testpagejllxselect = self.testpage.jllx_select     # ---活动奖励---# 奖励类型下拉框路径
        self.testpagewtjlp = self.testpage.w_tjlp    # ---活动奖励---# 未添加礼品时，“添加礼品”文字链接路径

        self.testpagecancelbutton = self.testpage.cancelbutton   #取消按钮
        self.testpagesubmitbutton = self.testpage.submitbutton   #提交按钮

        ######################创建优惠券页面###############################
        self.ticketcreatepage = TicketCreatePage()   #创建优惠券页
        self.ticketcreatepage_kcsl_input  = self.ticketcreatepage.kcsl_input   #第一部分# 库存数量输入框路径
        self.ticketcreatepage_qyxq_select = self.ticketcreatepage.qyxq_select   #第一部分# 券有效期选择框路径
        self.ticketcreatepage_yhqsm_areatext  = self.ticketcreatepage.yhqsm_areatext    #第一部分# 优惠券说明多行输入框路径
        self.ticketcreatepage_yhqmc_input = self.ticketcreatepage.yhqmc_input    #第二部分# 优惠券名称输入框路径
        self.ticketcreatepage_yhlx_select = self.ticketcreatepage.yhlx_select    #第二部分# 优惠类型选择框路径
        self.ticketcreatepage_yhms_select = self.ticketcreatepage.yhms_select    #第二部分# 优惠模式选择框路径
        self.ticketcreatepage_zdxf_input = self.ticketcreatepage.zdxf_input    #第二部分# 最低消费输入框路径
        self.ticketcreatepage_zfqdxz_select  = self.ticketcreatepage.zfqdxz_select     #第二部分# 支付渠道限制选择框路径
        self.ticketcreatepage_syfw_select   = self.ticketcreatepage.syfw_select     #第二部分# 使用范围选择框路径

        self.ticketcreatepage_confirm_button = self.ticketcreatepage.confirm_button   #页面 确定按钮

        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    def writexunicookie(self):
        addcookie = {'name': '.nereus.manager.settle.banks', 'value': 'QCK9GvKG8OEOh6lRUyyLlmKnHl8i3w'}
        self.activeweb.driver.add_cookie(addcookie)
        self.activeweb.driver.refresh()
        self.activeweb.delayTime(5)
        self.activeweb.outPutMyLog("写入虚拟银行cookie完成")

    #定义创建活动,
    #投放渠道为1表示内部渠道，为2表示外部渠道
    # 任务类型为1表示注册，为2表示交易，
    #奖励类型1表示固定奖励
    def definecreateactivity(self,num,tfqd,rwlx,jllx,ishaspresent,
                             hdmcinputtext,hdsjstarttimedataxpath,hdsjstarttimesecondsxpath,
                             hdsjendtimedataxpath,hdsjendtimesecondsxpath,
                             hdysinputtext,tfqdselectoptionxpath,hdbztextareainputtext,
                             rwlxselectoptionxpath,jllxselectoptionxpath):
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #创建活动
        #填入基础信息部分
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdmcinput, hdmcinputtext)   #输入活动名称
        self.activeweb.findElementByXpathAndClickAbountDataToSecound(num,self.testpagehdsjstarttime,hdsjstarttimedataxpath,hdsjstarttimesecondsxpath)   #点选活动时间开始时间
        self.activeweb.findElementByXpathAndClickAbountDataToSecound(num,self.testpagehdsjendtime ,hdsjendtimedataxpath, hdsjendtimesecondsxpath)   #点选活动时间结束时间
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdysinput, hdysinputtext)   #输入活动预算
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagetfqdselect,tfqdselectoptionxpath)  # 选项投放渠道一级渠道
        if tfqd == '1':    #点击投放渠道二级渠道复选框
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_app_checkbox)
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_web_checkbox)
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_sdk_checkbox)
        else:
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_app_checkbox)
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_web_checkbox)
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_sdk_checkbox)

        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdbztextarea, hdbztextareainputtext)   #输入活动备注

        #填入活动任务规则部分
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagerwlxselect,rwlxselectoptionxpath)  # 选项任务类型
        if rwlx=='2':
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_jylx_checkbox)  #点击交易类型全选框

        #填入活动奖励部分
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagejllxselect,jllxselectoptionxpath)  # 选择奖励类型
        self.activeweb.findElementByXpathAndClickNum(num, self.testpagewtjlp)  # 点击添加礼品文字链接(还未添加礼品)

        #进入创建优惠券页，新建优惠券
        #第一部分
        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.ffzt_kq_checkbox)  # 点击发放状态开始对应的选项框
        # self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage_kcsl_input, '') # 输入库存数量不输入
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.ticketcreatepage_qyxq_select,self.ticketcreatepage.qyxq_select_option_xdsj)  # 选择券有效期选项为相对时间
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage.qyxq_select_option_xdsj_ts_input, "2")  # 输入相对时间为2天
        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.yxcbcdf_pt_checkbox)  # 点击营销成本承担方中的平台前的选项框
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage_yhqsm_areatext, "开启-不限库存数-相对时间(相对2天)-平台-代金券-固定金额（面值2000）-不限最低消费-不限支付渠道-使用平台（点选QRindo）-不限使用范围-不可与其他活动叠加-支持退券")  # 输入优惠券说明
        #第二部分
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage_yhqmc_input,"优惠券_%s" % GetTimeStr().getTimeStr())  # 添加优惠券名称
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.ticketcreatepage_yhlx_select,self.ticketcreatepage.yhlx_option_djq)   #优惠类型选择代金券
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.ticketcreatepage_yhms_select,self.ticketcreatepage.yhms_select_option_gdje)   #优惠模式选择固定金额
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage.yhms_select_option_gdje_mz_input,"2000")  # 面值输入2000
        self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_QRindo_checkbox)  # 使用平台点选QRindo
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.ticketcreatepage_syfw_select,self.ticketcreatepage.syfw_select_option_bx)   #使用范围选择不限
        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.kfyqthddj_bkdjsy_checkbox)  # 可否与其他活动叠加点选不可叠加使用
        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.sfzctq_kt_checkbox)  # 是否支持退券点选可退

        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage_confirm_button)   #点击确定按钮
        ################################优惠券创建完成#########################################

        self.activeweb.findElementByXpathAndClickNum(num, self.testpagesubmitbutton)  # 点击提交按钮



    def defineasserttextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在text:%s"%testtext)

    def defineisintable(self,num,testtablexpath,expecttext,tablecolnum):
        notexsitflag = True
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, testtablexpath)
        for value in tabledic.values():
            # self.activeweb.outPutMyLog("%s"% value[int(tablecolnum)])
            if str(expecttext).lower() in value[int(tablecolnum)].lower():
                self.assertTrue(True)
                self.activeweb.outPutMyLog("在%s中存在text:%s"% (value[int(tablecolnum)],expecttext))
                notexsitflag = False
                break
        if notexsitflag:
            self.activeweb.outPutMyLog("在%s不存在：%s"% (tabledic,expecttext))
            self.assertTrue(False)



    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,tfqd,rwlx,jllx,ishaspresent,
                             hdmcinputtext,hdsjstarttimedataxpath,hdsjstarttimesecondsxpath,
                             hdsjendtimedataxpath,hdsjendtimesecondsxpath,
                             hdysinputtext,tfqdselectoptionxpath,hdbztextareainputtext,
                             rwlxselectoptionxpath,jllxselectoptionxpath):
        def func(self):
            self.definecreateactivity(num,tfqd,rwlx,jllx,ishaspresent,
                             hdmcinputtext,hdsjstarttimedataxpath,hdsjstarttimesecondsxpath,
                             hdsjendtimedataxpath,hdsjendtimesecondsxpath,
                             hdysinputtext,tfqdselectoptionxpath,hdbztextareainputtext,
                             rwlxselectoptionxpath,jllxselectoptionxpath)
        return func

def __generateTestCases():
    from addmerchant.models import AddMerchant

    addmerchant_all = AddMerchant.objects.filter(iscompany=False).order_by('id')
    rows_count = addmerchant_all.count()

    for addmerchant in addmerchant_all:

        if len(str(addmerchant.id)) == 1:
            addmerchantid = '0000%s'% addmerchant.id
        elif len(str(addmerchant.id)) == 2:
            addmerchantid = '000%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 3:
            addmerchantid = '00%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 4:
            addmerchantid = '0%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 5:
            addmerchantid = '%s' % addmerchant.id
        else:
            addmerchantid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(addmerchant.id)
        args.append(addmerchant.isfictitious)
        args.append("%s_%s"%(addmerchant.brandnameinputtext,GetTimeStr().getTimeStr()))
        args.append(addmerchant.emailinputtext)
        args.append(addmerchant.contactnumberinputtext)
        args.append(addmerchant.merchanttypeselectoptionxpath)
        args.append(addmerchant.categoryselectoptionxpath)
        args.append(addmerchant.criteriaselectoptionxpath)
        args.append(addmerchant.siupinputtext)
        args.append(addmerchant.provinceselectoptionxpath)
        args.append(addmerchant.cityselectoptionxpath)
        args.append(addmerchant.districtinputtext)
        args.append(addmerchant.villageinputtext)
        args.append(addmerchant.postcodeinputtext)
        args.append(addmerchant.addressinputtext)
        args.append(addmerchant.photosiupimagefilepath)
        args.append(addmerchant.photonpwpcompanyimagefilepath)
        args.append(addmerchant.phototdpimagefilepath)
        args.append(addmerchant.nameinputtext)
        args.append(addmerchant.npwpinputtext)
        args.append(addmerchant.typeidselectoptionxpath)
        args.append(addmerchant.identitynumberinputtext)
        args.append(addmerchant.address2inputtext)
        args.append(addmerchant.nationalityselectoptionxpath)
        args.append(addmerchant.phoneinputtext)
        args.append(addmerchant.email2inputtext)
        args.append(addmerchant.photofullfacebustimagefilepath)
        args.append(addmerchant.locationphotoimagefilepath)
        args.append(addmerchant.photoofthecashiersdeskimagefilepath)
        args.append(addmerchant.otherphotoimagefilepath)
        args.append(addmerchant.bankselectoptionxpath)
        args.append(addmerchant.accountnameinputtext)
        args.append(addmerchant.accountnumberinputtext)
        args.append(addmerchant.qrindoaccountinputtext)


        setattr(TestCreateActivityClass, 'test_func_%s_%s' % (addmerchantid,addmerchant.testcasetitle),
                TestCreateActivityClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

    # file_name = "D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\dataconfig\\assertselectsearchmanager.xls"
    # sheet_id = 0
    # datasheet = GetData(file_name,sheet_id)   #实例化
    # # rows_count = datasheet.get_case_lines()   #获取表的行数
    # for i in range(1, rows_count):  # 循环，但去掉第一
    #     args = []
    #     args.append(i)
    #     args.append(datasheet.is_cookie(i))
    #     args.append(datasheet.get_url(i))
    #     args.append(datasheet.get_selectxpath(i))
    #     args.append(datasheet.get_selectoptiontext(i))
    #     args.append(datasheet.get_selectinputxpath(i))
    #     args.append(datasheet.get_selectinputtext(i))
    #     args.append(datasheet.get_searchbuttonxpath(i))
    #     args.append(datasheet.get_searchtableresultxpath(i))
    #     args.append(datasheet.get_colnum(i))
    #     args.append(datasheet.get_checktext(i))
    #
    #
    #     setattr(TestSearchClass, 'test_func_%s_%s' % (datasheet.get_id(i),datasheet.get_title(i)),
    #             TestSearchClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










