import unittest

from webtestdata.settings import WEB_URL_TITLE,MANAGER_LOGIN_ACCOUNT,MANAGER_LOGIN_PASSWORD,MANAGER_REVIEW_MERCHANTID


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson

from TestCaseFunction.autotest.config.page.manager.loginPage import LoginPage
from TestCaseFunction.autotest.config.page.manager.merchantListPage import MerchantListPage
from TestCaseFunction.autotest.config.page.manager.reviewPage import ReviewPage



class TestReviewMerchantClass(unittest.TestCase):  # 创建测试类


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
        self.testpage = MerchantListPage()
        self.testpageurl = self.testpage.pageurl   #测试页面url
        self.testpagesearchbutton = self.testpage.searchbutton   #测试页面搜索按钮
        self.testpagesearchresultxpathtrue = self.testpage.searchtableresult   #测试页面找到相应数据结果xpath路径
        self.testpagesearchresultxpathfalse = self.testpage.searchtableresult2  #测试页面没有找到相应数据结果xpath路径

        #审核页
        self.reviewpage = ReviewPage()
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
                self.activeweb.outPutMyLog("在%s中存在文本信息：%s"% (value[int(colnum)],checktext))
                break
            else:
                self.activeweb.outPutMyLog("在%s不存在文本信息：%s"% (value[int(colnum)],checktext))
                self.assertTrue(False)

    #自动审核商户
    def testreviewmerchant(self):
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndInput(self.testpage.keywordselectinputxpath, str("ahditest_merchantfreya_R_individu"))  #输入框中输入“ahditest_merchantfreya_R_individu”
        self.activeweb.findElementByXpathAndReturnOptions(self.testpage.statusselectxpath, str("Waiting For Review"))
        self.activeweb.findElementByXpathAndClick(self.testpagesearchbutton)  #点击搜索按钮
        self.activeweb.findElementByXpathAndClick(self.testpage.reviewtextlinkxpath)   #点击“Review”
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.reviewpage.approvedbutton)  # 点击审核页“approved”
        self.activeweb.findElementByXpathAndClick(self.reviewpage.confirmbutton)  # 点击审核页第二页“confirm”
        #验证跳转到商户列表页
        self.activeweb.findElementByXpathAndReturnTextNotNum(self.testpagesearchbutton)



if __name__ == '__main__':
    print("hello world")
    unittest.main()










