import unittest

from webtestdata.settings import WEB_URL_TITLE,MANAGER_LOGIN_ACCOUNT,MANAGER_LOGIN_PASSWORD,MARKETING_CREATE_ACTIVITYID
from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE,TEST_MANAGER_LOGIN_ACCOUNT,TEST_MANAGER_LOGIN_PASSWORD   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE,ONLINE_MANAGER_LOGIN_ACCOUNT,ONLINE_MANAGER_LOGIN_PASSWORD  #导入现网环境参数


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
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityListPage import ActivityListPage   #导入活动列表页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityDetailsPage import ActivityDetialsPage #导入活动详情页




class TestInputTipClass(unittest.TestCase):  # 创建测试类


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

        if ISONLINE:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,ONLINE_MANAGER_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,ONLINE_MANAGER_LOGIN_PASSWORD)
        else:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,TEST_MANAGER_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,TEST_MANAGER_LOGIN_PASSWORD)

        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = ActivityCreatePage()
        self.testpageurl =self.testpage.pageurl   #测试页面url
        self.testpagesubmitbutton = self.testpage.submitbutton   #提交按钮

        self.testpagerwlxselect = self.testpage.rwlx_select  # ---活动任务规则---# 任务类型下拉框路径

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

        ######################活动列表页###############################
        self.activitylistpage = ActivityListPage()   #活动列表页
        self.activitylistpage_searchtableresult = self.activitylistpage.searchtableresult

        ######################待上线活动详情页###############################
        self.activitydetialspage = ActivityDetialsPage()   #活动列表页



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

    #定义inputtip函数
    def defineinputtip(self,num,isinput=None,inputxpath=None,
                       inputtext=None,inputtipxpath=None,inputtiptext=None):
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagerwlxselect,
                                                                self.testpage.rwlx_select_jx_option)  # 任务类型选择交易
        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tjxz)  # 点击添加限制文字链接
        self.activeweb.findElementByXpathAndClickNum(num,
                                                     self.testpage.rwmb_popup_yhhdcycs_option)  # 点击添加限制弹框中的用户活动参与次数

        #是否输入input内容
        if isinput:
            if inputxpath != None and inputtext !=None:
                self.activeweb.findElementByXpathAndInputNum(num, inputxpath, inputtext)  # 输入input内容

        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagesubmitbutton)  # 点击提交按钮
        self.defineasserttextnum(num,inputtipxpath,inputtiptext)   #断言tip实际内容是否与预期内容一致


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
                self.activeweb.outPutMyLog("在【%s】中存在:【%s】"% (value[int(tablecolnum)],expecttext))
                notexsitflag = False
                break
        if notexsitflag:
            self.activeweb.outPutMyLog("在【%s】不存在：【%s】"% (tabledic,expecttext))
            self.assertTrue(False)



    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,isinput,inputxpath,
                       inputtext,inputtipxpath,inputtiptext):
        def func(self):
            self.defineinputtip(num,isinput,inputxpath,
                       inputtext,inputtipxpath,inputtiptext)
        return func

def __generateTestCases():
    from inputtip.models import InputTipData

    inputtipdata_all = InputTipData.objects.filter(testproject="营销系统").filter(testmodule="任务活动管理").filter(testpage="创建活动_交易类型").order_by('id')
    rows_count = inputtipdata_all.count()

    for inputtipdata in inputtipdata_all:

        if len(str(inputtipdata.id)) == 1:
            inputtipdataid = '0000%s'% inputtipdata.id
        elif len(str(inputtipdata.id)) == 2:
            inputtipdataid = '000%s' % inputtipdata.id
        elif len(str(inputtipdata.id)) == 3:
            inputtipdataid = '00%s' % inputtipdata.id
        elif len(str(inputtipdata.id)) == 4:
            inputtipdataid = '0%s' % inputtipdata.id
        elif len(str(inputtipdata.id)) == 5:
            inputtipdataid = '%s' % inputtipdata.id
        else:
            inputtipdataid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(inputtipdata.id)
        args.append(inputtipdata.isinput)
        args.append(inputtipdata.inputxpath)
        args.append(inputtipdata.inputtext)
        args.append(inputtipdata.inputtipxpath)
        args.append(inputtipdata.inputtiptext)

        setattr(TestInputTipClass,
                'test_func_%s_%s_%s_%s(%s)' % (inputtipdataid,inputtipdata.testmodule,inputtipdata.testpage, inputtipdata.testcasetitle,inputtipdata.inputtiptext),
                TestInputTipClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










