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
from autotest.config.page.agent180.merchantListPage import MerchantListPage

merchantlist = MerchantListPage()

testdata = (
    (merchantlist.keyword,merchantlist.keywordtext),  #-----------筛选字段-----------#
    (merchantlist.status_shaixuan, merchantlist.status_shaixuan_text),
    (merchantlist.merchantnameid,merchantlist.merchantnameidtext),    #-----------表格title内容-----------#
    (merchantlist.loginaccount, merchantlist.loginaccounttext),
    (merchantlist.category,merchantlist.categorytext),
    (merchantlist.registrationtime, merchantlist.registrationtimetext),
    (merchantlist.status, merchantlist.statustext),
    (merchantlist.operation, merchantlist.operationtext),
)

testdatatwo = (
    (merchantlist.keywordtext,merchantlist.keywordselectxpath,merchantlist.keyword_merchantname,merchantlist.keyword_merchantname_text),   # -----------筛选字段keyword选项内容-----------#
    (merchantlist.keywordtext,merchantlist.keywordselectxpath, merchantlist.keyword_merchantid, merchantlist.keyword_merchantid_text),
    (merchantlist.keywordtext,merchantlist.keywordselectxpath, merchantlist.keyword_loginaccount, merchantlist.keyword_loginaccount_text),
    (merchantlist.status_shaixuan_text,merchantlist.statusselectxpath, merchantlist.status_all,  merchantlist.status_all_text),   # -----------筛选字段Status选项内容-----------#
    (merchantlist.status_shaixuan_text,merchantlist.statusselectxpath, merchantlist.status_waitingforreview, merchantlist.status_waitingforreview_text),
    (merchantlist.status_shaixuan_text,merchantlist.statusselectxpath, merchantlist.status_unapproved, merchantlist.status_unapproved_text),
    (merchantlist.status_shaixuan_text,merchantlist.statusselectxpath, merchantlist.status_normal, merchantlist.status_normal_text),
    (merchantlist.status_shaixuan_text,merchantlist.statusselectxpath, merchantlist.status_disabled, merchantlist.status_disabled_text),
)


class TestMerchantListClass(unittest.TestCase):  # 创建测试类


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
        cls.testpage = MerchantListPage()
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

    def defineassertselecttextnum(self,num,selecttext,selectxpath,testselectoptiontextxpath,expecttext):
        #断言是否存在某个选项文本
        self.activeweb.findElementByXpathAndScriptClickNum(num,selectxpath)
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testselectoptiontextxpath)
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在text:%s"%testtext)
        self.activeweb.findElementByXpathAndScriptClickNum(num, testselectoptiontextxpath)

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

    @staticmethod    #根据不同的参数生成测试用例
    def selectoptiontextcheck( num,selecttext,selectxpath,testselectoptiontextxpath,expecttext):
        def biangengfuncTwo(self):
            self.defineassertselecttextnum(num,selecttext,selectxpath,testselectoptiontextxpath,expecttext)
        return  biangengfuncTwo

def __generateTestCases():
    testdataall = testdata

    i = 1
    for testdataone in testdataall:

        if len(str(i)) == 1:
            casenum = '0000%s'% i
        elif len(str(i)) == 2:
            casenum = '000%s' % i
        elif len(str(i)) == 3:
            casenum = '00%s' % i
        elif len(str(i)) == 4:
            casenum = '0%s' % i
        elif len(str(i)) == 5:
            casenum = '%s' % i
        else:
            casenum ='i已经超过5位数，请重新定义'
        args=[]
        args.append(casenum)
        args.append(testdataone[0])
        args.append(testdataone[1])

        setattr(TestMerchantListClass, 'test_func_%s_%s_%s' % (u"列表表头和筛选字段文本检查",casenum,testdataone[1]),
                TestMerchantListClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
        i=i+1

def selectoptiontextchecktestcases():
    testdataall = testdatatwo

    i = 1
    for testdataone in testdataall:

        if len(str(i)) == 1:
            casenum = '0000%s'% i
        elif len(str(i)) == 2:
            casenum = '000%s' % i
        elif len(str(i)) == 3:
            casenum = '00%s' % i
        elif len(str(i)) == 4:
            casenum = '0%s' % i
        elif len(str(i)) == 5:
            casenum = '%s' % i
        else:
            casenum ='i已经超过5位数，请重新定义'
        args=[]
        args.append(casenum)
        args.append(testdataone[0])
        args.append(testdataone[1])
        args.append(testdataone[2])
        args.append(testdataone[3])

        setattr(TestMerchantListClass, 'test_func_%s_%s_%s_%s' % (u"筛选字段选项内容检查",casenum,testdataone[0],testdataone[3]),
                TestMerchantListClass.selectoptiontextcheck(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
        i=i+1

__generateTestCases()
selectoptiontextchecktestcases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










