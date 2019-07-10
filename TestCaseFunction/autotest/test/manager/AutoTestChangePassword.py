import unittest
import ddt

from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE,TEST_CHANGEPASSWORD_LOGIN_ACCOUNT,TEST_CHANGEPASSWORD_LOGIN_PASSWORD #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE,ONLINE_MANAGER_LOGIN_ACCOUNT,ONLINE_MANAGER_LOGIN_PASSWORD  #导入现网环境参数


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson

from TestCaseFunction.autotest.config.page.manager.loginPage import LoginPage
from TestCaseFunction.autotest.config.page.manager.changePasswordPage import ChangePasswordPage

dataout = (
        ("1",None,None,None,"This option cannot be empty","This option cannot be empty","This option cannot be empty"),  #输入为空提示
        ("2"," "," "," ","This option cannot be empty","This option cannot be empty","This option cannot be empty"),  #输入为空格提示，空格如何处理
        ("3","中","中","中","The length cannot be less than6","The length cannot be less than6","New password entered inconsistently"), #输入为汉字提示（类型提示与长度提示哪个先校验）
        ("4", "中国人寿保险公司", "中国人寿保险公司", "中国人寿保险公司", "Original password is incorrect", "仅支持字母数字符号","仅支持字母数字符号"),   #旧密码，输入在长度范围内的汉字时，是提示类型错误，还是提示密码错误
        ("5", "qwert", "qwert", "qwert","The length cannot be more than6", "The length cannot be more than6", "The length cannot be more than6"), #长度校验，小于6位
        ("6", "qwertyuiop1234567890#$%^&", "qwertyuiop1234567890#$%^&", "qwertyuiop1234567890#$%^&", "The length cannot be more than24", "The length cannot be more than24","The length cannot be more than24"),  #长度校验，大于24位
        # ("7", "123456", "中国人寿保险公司", "中国人寿保险公司", None, "仅支持字母数字符号","仅支持字母数字符号"),   #旧密码正确，新密码输入汉字
        # ("8", "123456", "1234 wer", "1234 wer", None, "仅支持字母数字符号","仅支持字母数字符号"),   #旧密码正确，新密码输入带有中间空格，密码中可以有空格吗？？？
        ("9", "123456", "1234qwer", "qwer1234", None, None,"New password entered inconsistently"),   #旧密码正确，新密码符合6-24位字母数字符号，确认密码与新密码不一致
)


@ddt.ddt   #使用ddt修饰测试类
class TestChangePasswordClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.activeweb = ActiveWeb()  # 实例化
        cls.loginurl = LoginPage().pageurl
        cls.activeweb.getUrl(cls.loginurl)  # 打开网址

        if ISONLINE:
            cls.activeweb.findElementByXpathAndInput(LoginPage().account,ONLINE_MANAGER_LOGIN_ACCOUNT)
            cls.activeweb.findElementByXpathAndInput(LoginPage().password,ONLINE_MANAGER_LOGIN_PASSWORD)
        else:
            cls.activeweb.findElementByXpathAndInput(LoginPage().account,TEST_CHANGEPASSWORD_LOGIN_ACCOUNT)
            cls.activeweb.findElementByXpathAndInput(LoginPage().password,TEST_CHANGEPASSWORD_LOGIN_PASSWORD)

        cls.activeweb.findElementByXpathAndScriptClick(LoginPage().loginbutton)
        cls.activeweb.delayTime(3)
        cls.testpage = ChangePasswordPage()
        # pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        cls.activeweb.closeBrowse()
        # pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        # self.testpageurl =self.testpage.pageurl   #测试页面url
        self.activeweb.getUrl(self.testpage.pageurl)
        self.activeweb.delayTime(3)
        # pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        # self.activeweb.closeBrowse()
        pass


    def definechangepassword(self,num,currentpasswordinputtext=None,newpasswordinputtext=None,
                             confirmpasswordinputtext=None,precurrentpasswordinputtiptext=None,
                             prenewpasswordinputtiptext=None,preconfirmpasswordinputtiptext=None):
        if currentpasswordinputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpage.currentpasswordinput,currentpasswordinputtext)
        if currentpasswordinputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpage.newpasswordinput,newpasswordinputtext)
        if currentpasswordinputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpage.confirmpasswordinput,confirmpasswordinputtext)

        self.activeweb.findElementByXpathAndClickNum(num,self.testpage.submitbutton)   #点击提交按钮
        if precurrentpasswordinputtiptext !=None:
            currentpasswordinputtiptext = self.activeweb.findElementByXpathAndReturnText(num,self.testpage.currentpasswordinputtip)
            self.assertEqual(precurrentpasswordinputtiptext,currentpasswordinputtiptext)
        if prenewpasswordinputtiptext !=None:
            newpasswordinputtiptext = self.activeweb.findElementByXpathAndReturnText(num,self.testpage.newpasswordinputtip)
            self.assertEqual(prenewpasswordinputtiptext,newpasswordinputtiptext)
        if preconfirmpasswordinputtiptext != None:
            confirmpasswordinputtiptext = self.activeweb.findElementByXpathAndReturnText(num,self.testpage.confirmpasswordinputtip)
            self.assertEqual(preconfirmpasswordinputtiptext,confirmpasswordinputtiptext)





    @ddt.data(*dataout)    #分离@ddt.data（）中的数据
    @ddt.unpack   #使用unpack表示可以传入2个以上的参数
    def test(self,*dataout):
        num,currentpasswordinputtext,newpasswordinputtext,confirmpasswordinputtext,precurrentpasswordinputtiptext,prenewpasswordinputtiptext,preconfirmpasswordinputtiptext = dataout
        self.definechangepassword(num,currentpasswordinputtext,newpasswordinputtext,confirmpasswordinputtext,precurrentpasswordinputtiptext,prenewpasswordinputtiptext,preconfirmpasswordinputtiptext)







if __name__ == '__main__':
    print("hello world")
    unittest.main()










