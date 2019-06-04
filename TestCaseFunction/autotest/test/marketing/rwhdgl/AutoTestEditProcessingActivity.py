import unittest

from webtestdata.settings import WEB_URL_TITLE,MANAGER_LOGIN_ACCOUNT,MANAGER_LOGIN_PASSWORD


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
# from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityCreatePage import ActivityCreatePage   #导入创建活动页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityEditPage import ActivityEditPage  #导入未上线活动编辑页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.ticketCreatePage import TicketCreatePage   #导入创建优惠券页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityListPage import ActivityListPage   #导入活动列表页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.processingActivityEditPage import ProcesingActivityEditPage   #导入进行中活动编辑页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.processingTicketEditPage import ProcessingTicketEditPage   #导入进行中活动编辑页


class TestEditProcessingActivityClass(unittest.TestCase):  # 创建测试类

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
        self.activeweb.findElementByXpathAndInput(LoginPage().account,MANAGER_LOGIN_ACCOUNT)
        self.activeweb.findElementByXpathAndInput(LoginPage().password,MANAGER_LOGIN_PASSWORD)
        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = ProcesingActivityEditPage()
        self.testpageurl =self.testpage.pageurl   #测试页面url

        self.testpagehdsjendtime = self.testpage.hdsj_endtime  # ---基础信息---#   活动时间结束时间输入框路径
        self.testpagehdyszjysinput  = self.testpage.hdys_zjys_input   # ---基础信息---#   增加预算输入框路径

        self.testpagejllpedit = self.testpage.y_jllp_table_cz_just_one_edit   # ---活动奖励---#   券“编辑”文字链接


        self.testpagecancelbutton = self.testpage.cancelbutton   #取消按钮
        self.testpagesubmitbutton = self.testpage.submitbutton   #提交按钮

        ######################编辑优惠券页面###############################
        self.processingticketeditpage = ProcessingTicketEditPage()   #进行中的活动的编辑优惠券页


        ######################活动列表页###############################
        self.activitylistpage = ActivityListPage()   #活动列表页
        self.activitylistpage_searchtableresult = self.activitylistpage.searchtableresult


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
    #投放渠道一级为1表示内部渠道，为2表示外部渠道
    #投放渠道二级为0表示全选，为1，2，等表示选一项和选多项组合，程序中只有全选和选择一项的情况
    # 任务类型为1表示注册，为2表示交易类型
    #奖励类型1表示固定奖励
    def defineeditprocessingactivity(self,num,
                           zjysinputtext,ffzt,zjkcinputtext,isqcancel,iscancel):
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #创建活动
        #填入基础信息部分
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClickAbountData(num,self.testpagehdsjendtime,self.testpage.hdsj_endtime_daytime,pathright=self.testpage.hdsj_endtime_rightmove,pathconfirm=self.testpage.hdsj_endtime_queding)   #点选活动时间结束时间

        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdyszjysinput, zjysinputtext)   #输入活动增加预算


        #填入活动奖励部分
        self.activeweb.findElementByXpathAndClickNum(num, self.testpagejllpedit)  # 点击添加礼品中的“编辑”文字按钮

        #进入编辑优惠券页，编辑优惠券
        if ffzt == "1":
            self.activeweb.findElementByXpathAndClickNum(num, self.processingticketeditpage.ffzt_kq_checkbox)  # 点击发放状态开始对应的选项框
        else:
            self.activeweb.findElementByXpathAndClickNum(num, self.processingticketeditpage.ffzt_gb_checkbox)  # 点击发放状态关闭对应的选项框

        self.activeweb.findElementByXpathAndInputNum(num, self.processingticketeditpage.kcsl_zjkc_input, zjkcinputtext)  # 输入增加库存

        # self.activeweb.delayTime(5000)



        if isqcancel:
            self.activeweb.findElementByXpathAndScriptClickNum(num,
                                                                   self.processingticketeditpage.cancel_button_zdhy)  # 点击取消按钮
        else:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.processingticketeditpage.confirm_button_zdhy)   #点击确定按钮

        ################################优惠券创建完成#########################################

        #断言优惠券编辑后的发放状态
        ffzt_text = self.activeweb.findElementByXpathAndReturnText(num,self.testpage.y_jllp_table_ffzt_result_just_one)
        print("ffzt_text:%s" % ffzt_text)
        if ffzt == "1":
            self.assertEqual("开启",ffzt_text)
        else:
            self.assertEqual("关闭", ffzt_text)

        # self.activeweb.delayTime(1000)


        if iscancel:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagecancelbutton)  # 点击取消按钮
        else:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagesubmitbutton)  # 点击提交按钮
            # 断言处于活动列表页
            xjhd_text = self.activeweb.findElementByXpathAndReturnText(num,self.activitylistpage.xjhd_button_text)
            self.assertEqual(self.activitylistpage.xjhd_button_text_text, xjhd_text)





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
    def getTestFunc(num,zjysinputtext,ffzt,zjkcinputtext,isqcancel,iscancel):
        def func(self):
            self.defineeditprocessingactivity(num,zjysinputtext,ffzt,zjkcinputtext,isqcancel,iscancel)
        return func

def __generateTestCases():
    from processingActivity.models import ProcessActivity

    processactivity_all = ProcessActivity.objects.filter(testproject="营销系统").filter(testmodule="任务活动管理").filter(testpage="编辑活动").filter(id=2).order_by('id')
    rows_count = processactivity_all.count()

    for processactivity in processactivity_all:

        if len(str(processactivity.id)) == 1:
            processactivityid = '0000%s'% processactivity.id
        elif len(str(processactivity.id)) == 2:
            processactivityid = '000%s' % processactivity.id
        elif len(str(processactivity.id)) == 3:
            processactivityid = '00%s' % processactivity.id
        elif len(str(processactivity.id)) == 4:
            processactivityid = '0%s' % processactivity.id
        elif len(str(processactivity.id)) == 5:
            processactivityid = '%s' % processactivity.id
        else:
            processactivityid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(processactivity.id)
        args.append(processactivity.zjysinputtext)
        args.append(processactivity.ffzt)
        args.append(processactivity.zjkcinputtext)
        args.append(processactivity.isqcancel)
        args.append(processactivity.iscancel)

        setattr(TestEditProcessingActivityClass, 'test_func_%s_%s' % (processactivityid,processactivity.testcasetitle),
                TestEditProcessingActivityClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










