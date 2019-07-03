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

from autotest.config.page.agent180.loginPage import LoginPage
from autotest.config.page.agent180.commonPage import CommonPage


class TestLogoutClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.activeweb = ActiveWeb()  # 实例化
        cls.loginurl = LoginPage().pageurl
        cls.activeweb.getUrl(cls.loginurl)  # 打开网址

        if ISONLINE:
            cls.activeweb.findElementByXpathAndInput(LoginPage().account,ONLINE_AGENT_LOGIN_ACCOUNT)
            cls.activeweb.findElementByXpathAndInput(LoginPage().password,ONLINE_AGENT_LOGIN_PASSWORD)
        else:
            cls.activeweb.findElementByXpathAndInput(LoginPage().account,TEST_AGENT_LOGIN_ACCOUNT)
            cls.activeweb.findElementByXpathAndInput(LoginPage().password,TEST_AGENT_LOGIN_PASSWORD)

        cls.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        cls.activeweb.delayTime(3)
        cls.testpage = CommonPage()
        # cls.testpageurl =cls.testpage.pageurl   #测试页面url
        # cls.activeweb.getUrl(cls.testpageurl)
        # cls.activeweb.delayTime(3)

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


    def testLogout(self):
        self.activeweb.findElementByXpathAndScriptClick(self.testpage.headportrait)
        self.activeweb.findElementByXpathAndScriptClick(self.testpage.logout)
        self.activeweb.findElementByXpathAndReturnTextNotNum(LoginPage().loginbutton)


if __name__ == '__main__':
    print("hello world")
    unittest.main()










