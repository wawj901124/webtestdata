import unittest

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
from TestCaseFunction.autotest.config.page.marketing.yyhdgl.activityListPage import ActivityListPage   #导入活动列表页


class TestDownLinesActivityClass(unittest.TestCase):  # 创建测试类

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
        self.testpage = ActivityListPage()
        self.testpageurl =self.testpage.pageurl   #测试页面url




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
    def definedownlinesactivity(self,num,sxhdmcinputtext,hdmcinputtext):
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #在活动名称中输入需要的活动ID
        self.activeweb.findElementByXpathAndInput(self.testpage.sx_hdmc_input, str(sxhdmcinputtext))   #在活动名称中输入需要的活动ID
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpage.sx_hdmc_input_list_one)   #点击输入框中筛选到的内容
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpage.cx_button)   #点击查询按钮
        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpage.table_justone_content_sx)  # 点击下线按钮
        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpage.first_sx_popup_qd)  # 点击下线弹框中确定
        #断言待上线活动变为进行中
        self.defineisintable(num, self.testpage.searchtableresult, hdmcinputtext, 4)


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
    def getTestFunc(num,sxhdmcinputtext,hdmcinputtext):
        def func(self):
            self.definedownlinesactivity(num,sxhdmcinputtext,hdmcinputtext)
        return func

# def __generateTestCases():
#     from addactivity.models import AddActivity
#
#     addactivity_all = AddActivity.objects.filter(testproject="营销系统").filter(testmodule="任务活动管理").filter(testpage="创建活动").filter(id=2).order_by('id')
#     rows_count = addactivity_all.count()
#
#     for addactivity in addactivity_all:
#
#         if len(str(addactivity.id)) == 1:
#             addactivityid = '0000%s'% addactivity.id
#         elif len(str(addactivity.id)) == 2:
#             addactivityid = '000%s' % addactivity.id
#         elif len(str(addactivity.id)) == 3:
#             addactivityid = '00%s' % addactivity.id
#         elif len(str(addactivity.id)) == 4:
#             addactivityid = '0%s' % addactivity.id
#         elif len(str(addactivity.id)) == 5:
#             addactivityid = '%s' % addactivity.id
#         else:
#             addactivityid ='Id已经超过5位数，请重新定义'
#
#
#         args = []
#         args.append(addactivity.id)
#         args.append("%s_%s"%(addactivity.hdmcinputtext,GetTimeStr().getTimeStr()))
#         args.append(addactivity.hdysinputtext)
#         args.append(addactivity.tfqdyj)
#         args.append(addactivity.tfqdej)
#         args.append(addactivity.hdbztextareainputtext)
#         args.append(addactivity.rwlx)
#         args.append(addactivity.tjrwxz)
#         args.append(addactivity.jyjylx)
#         args.append(addactivity.jyzffs)
#         args.append(addactivity.jymgyhzdcycsinputtext)
#         args.append(addactivity.jymgyhmrcycsinputtext)
#         args.append(addactivity.jllx)
#         args.append(addactivity.iscancel)
#
#         setattr(TestHighLinesActivityClass, 'test_func_%s_%s' % (addactivityid,addactivity.testcasetitle),
#                 TestHighLinesActivityClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
#
#     # file_name = "D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\dataconfig\\assertselectsearchmanager.xls"
#     # sheet_id = 0
#     # datasheet = GetData(file_name,sheet_id)   #实例化
#     # # rows_count = datasheet.get_case_lines()   #获取表的行数
#     # for i in range(1, rows_count):  # 循环，但去掉第一
#     #     args = []
#     #     args.append(i)
#     #     args.append(datasheet.is_cookie(i))
#     #     args.append(datasheet.get_url(i))
#     #     args.append(datasheet.get_selectxpath(i))
#     #     args.append(datasheet.get_selectoptiontext(i))
#     #     args.append(datasheet.get_selectinputxpath(i))
#     #     args.append(datasheet.get_selectinputtext(i))
#     #     args.append(datasheet.get_searchbuttonxpath(i))
#     #     args.append(datasheet.get_searchtableresultxpath(i))
#     #     args.append(datasheet.get_colnum(i))
#     #     args.append(datasheet.get_checktext(i))
#     #
#     #
#     #     setattr(TestSearchClass, 'test_func_%s_%s' % (datasheet.get_id(i),datasheet.get_title(i)),
#     #             TestSearchClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

def __generateTestCases():
        i = 1
        filename = "createactivityid.txt"
        activityid = GetTimeStr().readText(filename)
        sxhdmcinputtext = activityid
        hdmcinputtext = u"已结束"
        args = []
        args.append(i)
        args.append(sxhdmcinputtext)
        args.append(hdmcinputtext)


        setattr(TestDownLinesActivityClass, 'test_func_%s_%s' % (sxhdmcinputtext,hdmcinputtext),
                TestDownLinesActivityClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










