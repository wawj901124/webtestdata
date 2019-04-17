import unittest

from webtestdata.settings import WEB_URL_TITLE,MANAGER_LOGIN_ACCOUNT,MANAGER_LOGIN_PASSWORD,MANAGER_REVIEW_MERCHANTID


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

from TestCaseFunction.autotest.config.page.manager.loginPage import LoginPage
from TestCaseFunction.autotest.config.page.manager.reviewPage import ReviewPage
from autotest.config.page.manager.merchantListPage import MerchantListPage


class TestReviewClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        # cls.activeweb = ActiveWeb()  # 实例化
        # cls.loginurl = LoginPage().pageurl
        # cls.activeweb.getUrl(cls.loginurl)  # 打开网址
        # cls.activeweb.findElementByXpathAndInput(LoginPage().account,AGENT_LOGIN_ACCOUNT)
        # cls.activeweb.findElementByXpathAndInput(LoginPage().password,AGENT_LOGIN_PASSWORD)
        # cls.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        # cls.activeweb.delayTime(3)
        # cls.testpage = RevisePage()
        # cls.testpageurl =cls.testpage.pageurl   #测试页面url
        # cls.activeweb.getUrl(cls.testpageurl)
        # cls.activeweb.delayTime(3)

        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        # cls.activeweb.closeBrowse()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = LoginPage().pageurl
        self.activeweb.getUrl(self.loginurl)  # 打开网址
        self.activeweb.findElementByXpathAndInput(LoginPage().account,MANAGER_LOGIN_ACCOUNT)
        self.activeweb.findElementByXpathAndInput(LoginPage().password,MANAGER_LOGIN_PASSWORD)
        self.activeweb.findElementByXpathAndScriptClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = ReviewPage()
        # self.testpageurl =self.testpage.pageurl   #测试页面url
        self.activeweb.getUrl(MerchantListPage().pageurl)
        self.activeweb.delayTime(3)
        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        pass


    def defineclickturndown(self,num,reviewnoteinputtext):
        self.definesearch(num,
                          MerchantListPage().keywordselectxpath,
                          MerchantListPage().keywordoption_merchantid_text,
                          MerchantListPage().keywordselectinputxpath,
                          MANAGER_REVIEW_MERCHANTID,
                          True,
                          6,
                          "Review")
        #点击Review
        self.activeweb.findElementByXpathAndScriptClick(MerchantListPage().firstdatareview)
        #输入拒绝内容
        self.activeweb.findElementByXpathAndInput(self.testpage.reviewnoteinput,reviewnoteinputtext)
        #获取输入的内容
        self.activeweb.findElementByXpathAndReturnText(num,self.testpage.reviewnoteinput)
        #点击拒绝按钮
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpage.turndownbutton)


        # self.activeweb.delayTime(1000)


    def defineasserttextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在文本信息：%s"%testtext)

    def defineisintable(self,num,testtablexpath,expecttext,tablecolnum):
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, testtablexpath)
        for value in tabledic.values():
            self.activeweb.outPutMyLog("%s"% value[int(tablecolnum)])
            if str(expecttext).lower() in value[int(tablecolnum)].lower():
                self.assertTrue(True)
                self.activeweb.outPutMyLog("在%s中存在文本信息：%s"% (value[int(tablecolnum)],expecttext))
                break
            else:
                self.activeweb.outPutMyLog("在%s不存在文本信息：%s"% (value[int(tablecolnum)],expecttext))
                self.assertTrue(False)

    #定义搜索查找函数
    def definesearch(self,num,selectxpath=None,selectoptiontext=None,selectinputxpath=None,selectinputtext=None,isfind=False,colnum=None,checktext=None):

        if selectxpath !=None and selectoptiontext !=None:
            # self.activeweb.findElementByXpathAndScriptClick(selectxpath)
            # self.activeweb.findElementByXpathAndScriptClick(selectoptiontextxpath)
            self.activeweb.findElementByXpathAndReturnOptionsNum(num,selectxpath,str(selectoptiontext))

        if selectinputxpath != None and selectinputtext !=None:
            self.activeweb.findElementByXpathAndInput(selectinputxpath,str(selectinputtext))
        self.activeweb.findElementByXpathAndClick(MerchantListPage().searchbutton)
        self.activeweb.delayTime(5)
        if isfind:
            tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num,MerchantListPage().searchtableresult)
        else:
            tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, MerchantListPage().searchtableresult2)

        for value in tabledic.values():
            if str(checktext).lower() in value[int(colnum)].lower():
                self.assertTrue(True)
                self.activeweb.outPutMyLog("在%s中存在文本信息：%s"% (value[int(colnum)],checktext))
                break
            else:
                self.activeweb.outPutMyLog("在%s不存在文本信息：%s"% (value[int(colnum)],checktext))
                self.assertTrue(False)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,reviewnoteinputtext):
        def func(self):
            self.defineclickturndown(num,reviewnoteinputtext)
        return func

def __generateTestCases():
    testdataall = [(0,u"自动化测试拒绝"),]

    for testdataone in testdataall:

        args = testdataone

        setattr(TestReviewClass, 'test_func_%s_%s' % (testdataone[0],testdataone[1]),
                TestReviewClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










