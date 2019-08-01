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

from TestCaseFunction.autotest.config.page.agent.loginPage import LoginPage
from TestCaseFunction.autotest.config.page.agent.merchantListPage import MerchantListPage



class TestMerchantListClass(unittest.TestCase):  # 创建测试类


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
        self.testpageurl = MerchantListPage().pageurl   #测试页面url
        self.testpagesearchbutton = MerchantListPage().searchbutton   #测试页面搜索按钮
        self.testpagesearchresultxpathtrue = MerchantListPage().searchtableresult   #测试页面找到相应数据结果xpath路径
        self.testpagesearchresultxpathfalse = MerchantListPage().searchtableresult2  #测试页面没有找到相应数据结果xpath路径
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        pass

    #定义搜索查找函数
    def definesearch(self,num,selectxpath=None,selectoptiontextxpath=None,selectinputxpath=None,selectinputtext=None,isfind=False,colnum=None,checktext=None):
        # self.activeweb.writerCookies(self.cookie, LoginPage().pageurl,MerchantListPage().pageurl)
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        if selectxpath !=None and selectoptiontextxpath !=None:
            self.activeweb.findElementByXpathAndScriptClick(selectxpath)
            self.activeweb.findElementByXpathAndScriptClick(selectoptiontextxpath)

            # self.activeweb.findElementByXpathAndReturnOptions(selectxpath,str(selectoptiontext))
        if selectinputxpath != None and selectinputtext !=None:
            self.activeweb.findElementByXpathAndInput(selectinputxpath,str(selectinputtext))
        self.activeweb.findElementByXpathAndClick(self.testpagesearchbutton)
        self.activeweb.delayTime(5)
        if isfind:
            tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num,self.testpagesearchresultxpathtrue)
        else:
            tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, self.testpagesearchresultxpathfalse)
        for value in tabledic.values():
            if str(checktext).lower() in value[int(colnum)].lower():
                self.assertTrue(True)
                self.activeweb.outPutMyLog("在【%s】中存在:【%s】" % (value[int(colnum)], checktext))
            else:
                self.activeweb.outPutMyLog("在【%s】中不存在:【%s】" % (value[int(colnum)], checktext))
                self.assertTrue(False)


    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,selectxpath,selectoptiontextxpath,selectinputxpath,selectinputtext,isfind,colnum,checktext):
        def func(self):
            self.definesearch(num,selectxpath,selectoptiontextxpath,selectinputxpath,selectinputtext,isfind,colnum,checktext)
        return func

def __generateTestCases():
    from searchdata.models import SearchData

    searchdata_all = SearchData.objects.filter(webproject=u"Vue代理商web后台").filter(testpage=u"MerchantList").order_by('id')
    rows_count = searchdata_all.count()

    for searchdata in searchdata_all:

        if len(str(searchdata.id)) == 1:
            searchdataid = '0000%s'%searchdata.id
        elif len(str(searchdata.id)) == 2:
            searchdataid = '000%s' % searchdata.id
        elif len(str(searchdata.id)) == 3:
            searchdataid = '00%s' % searchdata.id
        elif len(str(searchdata.id)) == 4:
            searchdataid = '0%s' % searchdata.id
        elif len(str(searchdata.id)) == 5:
            searchdataid = '%s' % searchdata.id
        else:
            searchdataid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(searchdata.id)
        args.append(searchdata.selectxpath)
        args.append(searchdata.selectoptiontextxpath)
        args.append(searchdata.selectinputxpath)
        args.append(searchdata.selectinputtext)
        args.append(searchdata.isfind)
        args.append(searchdata.colnum)
        args.append(searchdata.checktext)


        setattr(TestMerchantListClass, 'test_func_%s_%s_%s' % (searchdataid,searchdata.testpage,searchdata.testcasetitle),
                TestMerchantListClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










