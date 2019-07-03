import unittest

# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from autotest.config.page.agent180.loginPage import LoginPage



class TestLoginClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.activeweb = ActiveWeb()  # 实例化
        self.loginpage = LoginPage()  # 实例化
        self.activeweb.getUrl(self.loginpage.pageurl)  # 打开网址
        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        pass

    # 定义登录函数
    def definelogin(self,num,accountinput=None,passwordinput=None,vercodeinput=None,assertaccounttiptext=None,
                    assertpasswordtiptext=None,assertvercodetiptext=None,assertlogintiptext=None):
        #1.进入登录页面
        #2.点击登录按钮
        #3.查看提示（输入框下方提示）
        if accountinput!=None:
            self.activeweb.findElementByXpathAndInput(path=self.loginpage.account,inputcontent=accountinput) #输入账号
        if passwordinput!=None:
            self.activeweb.findElementByXpathAndInput(path=self.loginpage.password,inputcontent= passwordinput) # 输入密码

        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)   #单击登录按钮

        #验证账号弹框下提示内容
        if assertaccounttiptext!=None:
            truetext = self.activeweb.findElementByXpathAndReturnText(num=num,path=self.loginpage.accounttip)
            self.assertEqual(assertaccounttiptext,truetext)

        # 验证密码弹框下提示内容
        if assertpasswordtiptext!=None:
            truetext = self.activeweb.findElementByXpathAndReturnText(num=num,path=self.loginpage.passwordtip)
            self.assertEqual(assertpasswordtiptext,truetext)

        # 验证验证码弹框下提示内容
        if assertvercodetiptext!=None:
            if vercodeinput != None:
                self.activeweb.findElementByXpathAndInput(path=self.loginpage.vercode,
                                                          inputcontent=vercodeinput)  # 输入验证码
            # print("验证码预期提示内容:%s" % assertvercodetiptext)
            self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton2)  # 单击登录按钮
            truetext = self.activeweb.findElementByXpathAndReturnText(num=num,path=self.loginpage.vercodetip)
            self.assertEqual(assertvercodetiptext,truetext)

        # 验证点击登录按钮后，服务端返回的提示内容
        if assertlogintiptext!=None:
            if vercodeinput != None:
                self.activeweb.findElementByXpathAndInput(path=self.loginpage.vercode,
                                                          inputcontent=vercodeinput)  # 输入验证码
                self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton2)  # 单击登录按钮

            truetext = self.activeweb.findElementByXpathAndReturnText(num=num,path=self.loginpage.logintip)
            self.assertEqual(assertlogintiptext,truetext)


    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,accountinput,passwordinput,vercodeinput,assertaccounttiptext,
                    assertpasswordtiptext,assertvercodetiptext,assertlogintiptext):
        def func(self):
            self.definelogin(num,accountinput,passwordinput,vercodeinput,assertaccounttiptext,
                    assertpasswordtiptext,assertvercodetiptext,assertlogintiptext)
        return func


def __generateTestCases():
    from logindata.models import LoginData

    logindata_all = LoginData.objects.all().order_by('id')
    rows_count = logindata_all.count()

    for logindata in logindata_all:
        if len(str(logindata.id)) == 1:
            logindataid = '0000%s'%logindata.id
        elif len(str(logindata.id)) == 2:
            logindataid = '000%s' % logindata.id
        elif len(str(logindata.id)) == 3:
            logindataid = '00%s' % logindata.id
        elif len(str(logindata.id)) == 4:
            logindataid = '0%s' % logindata.id
        elif len(str(logindata.id)) == 5:
            logindataid = '%s' % logindata.id
        else:
            logindataid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(logindata.id)
        # args.append(testsearch.is_cookie)
        # args.append("%s%s" % (WEB_URL_TITLE,testsearch.modulepage.ele_page_url))
        args.append(logindata.accountinput)
        args.append(logindata.passwordinput)
        args.append(logindata.vercodeinput)
        args.append(logindata.assertaccounttiptext)
        args.append(logindata.assertpasswordtiptext)
        args.append(logindata.assertvercodetiptext)
        args.append(logindata.assertlogintiptext)


        setattr(TestLoginClass, 'test_func_%s_%s' % (logindataid,logindata.testcasetitle),
                TestLoginClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










