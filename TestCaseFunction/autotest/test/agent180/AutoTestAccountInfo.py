import unittest

from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_AGENT_LOGIN_ACCOUNT,TEST_AGENT_LOGIN_PASSWORD   #导入测试环境参数
from webtestdata.settings import ONLINE_AGENT_LOGIN_ACCOUNT,ONLINE_AGENT_LOGIN_PASSWORD  #导入现网环境参数


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import ddt

from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson
from TestCaseFunction.util.gettimestr import GetTimeStr

from TestCaseFunction.autotest.config.page.agent180.loginPage import LoginPage
from autotest.config.page.agent180.accountInfoPage import AccountInfoPage

accountinfo = AccountInfoPage()

testpagebasicinfo = accountinfo.basicinfo
testpagebasicinfotext = accountinfo.basicinfotext
testpageagentid = accountinfo.agentid
testpageagentidtext = accountinfo.agentidtext
testpageloginaccount = accountinfo.loginaccount
testpageloginaccounttext = accountinfo.loginaccounttext

testpageagentname = accountinfo.agentname
testpageagentnametext = accountinfo.agentnametext
testpageagenttype = accountinfo.agenttype
testpageagenttypetext = accountinfo.agenttypetext
testpageagentidvalue = accountinfo.agentidvalue
testpageagentidvaluetext = accountinfo.agentidvaluetext

testpageloginaccountvalue = accountinfo.loginaccountvalue
testpageloginaccountvaluetext = accountinfo.loginaccountvaluetext
testpageagentnamevalue = accountinfo.agentnamevalue
testpageagentnamevaluetext = accountinfo.agentnamevaluetext
testpageagenttypevalue = accountinfo.agenttypevalue
testpageagenttypevaluetext = accountinfo.agenttypevaluetext
testdata = (
    ('01', testpagebasicinfo, testpagebasicinfotext),
    ('02', testpageagentid, testpageagentidtext),
    ('03', testpageloginaccount, testpageloginaccounttext),

    ('04', testpageagentname, testpageagentnametext),
    ('05', testpageagenttype, testpageagenttypetext),
    ('06', testpageagentidvalue, testpageagentidvaluetext),

    ('07', testpageloginaccountvalue, testpageloginaccountvaluetext),
    ('08', testpageagentnamevalue, testpageagentnamevaluetext),
    ('09', testpageagenttypevalue, testpageagenttypevaluetext),

)


class TestAccountInfoClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.activeweb = ActiveWeb()  # 实例化
        cls.loginurl = LoginPage().pageurl
        cls.activeweb.getUrl(cls.loginurl)  # 打开网址\

        if ISONLINE:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,ONLINE_AGENT_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,ONLINE_AGENT_LOGIN_PASSWORD)
        else:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,TEST_AGENT_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,TEST_AGENT_LOGIN_PASSWORD)

        cls.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        cls.activeweb.delayTime(3)
        cls.testpage = AccountInfoPage()
        cls.testpageurl =cls.testpage.pageurl   #测试页面url
        cls.activeweb.getUrl(cls.testpageurl)
        cls.activeweb.delayTime(3)

        # pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        cls.activeweb.closeBrowse()
        # pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        # self.activeweb.closeBrowse()
        pass


    def defineasserttextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在text:%s"%testtext)

    def defineisintable(self,num,testtablexpath,expecttext,tablecolnum):
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, testtablexpath)
        for value in tabledic.values():
            self.activeweb.outPutMyLog("%s"% value[int(tablecolnum)])
            if str(expecttext).lower() in value[int(tablecolnum)].lower():
                self.assertTrue(True)
                self.activeweb.outPutMyLog("在%s中存在text:%s"% (value[int(tablecolnum)],expecttext))
                break
            else:
                self.activeweb.outPutMyLog("在%s不存在：%s"% (value[int(tablecolnum)],expecttext))
                self.assertTrue(False)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc( num,testelexpath,expecttext):
        def func(self):
            self.defineasserttextnum(num,testelexpath,expecttext)
        return func

def __generateTestCases():
    testdataall = testdata

    for testdataone in testdataall:

        args = testdataone

        setattr(TestAccountInfoClass, 'test_func_%s_%s' % (testdataone[0],testdataone[2]),
                TestAccountInfoClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










