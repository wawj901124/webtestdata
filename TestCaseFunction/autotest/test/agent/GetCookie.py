# ----------------------------------------------------------------------
import os, django,sys
pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson
from pageelement.models import PageEle, ModulePage
from webtestdata.settings import WEB_URL_TITLE

class GetCookie():
    def __init__(self,outjsonfile=None,outloginurl=None,outloginaccountxpath=None,
                 outloginaccounttext=None,outloginppasswordxpath=None,outloginpasswordtext=None,
                 outloginbuttonxpath=None):

        if outjsonfile==None:
            self.jsonfile = '../cookiejson/cookiemanager.json'
        else:
            self.jsonfile = outjsonfile

        if outloginurl==None:
            self.loginurl ="https://bjw.halodigit.com:9090/nereus/manager/index#/login"
        else:
            self.loginurl = outloginurl

        if outloginaccountxpath==None:
            self.loginaccountxpath = "/html/body/div[1]/div[2]/form/div/div[1]/input"
        else:
            self.loginaccountxpath = outloginaccountxpath

        if outloginaccounttext==None:
            self.loginaccount = "xiangkaizheng@iapppay.com"
        else:
            self.loginaccount = outloginaccounttext

        if outloginppasswordxpath==None:
            self.loginppasswordxpath = "/html/body/div[1]/div[2]/form/div/div[2]/input"
        else:
            self.loginppasswordxpath = outloginppasswordxpath

        if outloginpasswordtext==None:
            self.loginpassword = "123456"
        else:
            self.loginpassword = outloginpasswordtext

        if outloginbuttonxpath==None:
            self.loginbuttonxpath = "/html/body/div[1]/div[2]/form/div/a[1]/span"
        else:
            self.loginbuttonxpath = outloginbuttonxpath

        self.operationjson = OperationJson(file_path=self.jsonfile)   #实例化
        self.activeweb = ActiveWeb()  # 实例化


    def getCookie(self):
        # 登录
        self.activeweb.getUrl(self.loginurl)  # 打开网址
        self.activeweb.findElementByXpathAndInput(self.loginaccountxpath,self.loginaccount)
        self.activeweb.findElementByXpathAndInput(self.loginppasswordxpath,self.loginpassword)
        self.activeweb.findElementByXpathAndClick(self.loginbuttonxpath)
        self.activeweb.delayTime(3)
        if 'merchant' in self.jsonfile :
            print("outjsonfile为：%s"% self.jsonfile)
            self.selectMerchant()
        else:
            print("开始获取cookie---")
        # 获取cookie
        cookie = self.activeweb.getCookies()
        self.activeweb.closeBrowse()
        return cookie

    def writerCookieToJson(self):
        self.cookie = self.getCookie()
        self.operationjson.write_data(self.cookie)
        print("\ncookie信息‘%s’已经写入‘%s’文件里。\n" % (self.cookie,self.jsonfile))

    #选商户时的操作
    def selectMerchant(self):
        self.merchantxpath = '/html/body/div[1]/div[2]/div/form/div[5]/p[1]/span/input'
        self.confirmbuttonxpath = '/html/body/div[1]/div[2]/div/form/div[43]/p/span[2]/button'

        self.activeweb.findElementByXpathAndScriptClick(self.merchantxpath)
        self.activeweb.findElementByXpathAndClick(self.confirmbuttonxpath)
        self.activeweb.delayTime(3)


if __name__ == '__main__':
    from pageelement.models import PageEle,ModulePage
    from webtestdata.settings import WEB_URL_TITLE

    testproject = u"印尼钱包商户管理平台"
    testmodule = u"账号登录"
    testpage = u"login"

    login_modulepages = ModulePage.objects.filter(testproject__web_project=testproject).filter(projectmodule__web_module=testmodule).filter(ele_page=testpage)

    for login_modulepage in login_modulepages:
        login_modulepage_url =login_modulepage.ele_page_url
        login_modulepage_id  = login_modulepage.id

    login_pageeles = PageEle.objects.filter(modulepage_id=login_modulepage_id)
    for login_pageele in login_pageeles:
        if login_pageele.ele_name=='AccountInput':
            login_pageeles_account_xpath = login_pageele.ele_xpath
        if login_pageele.ele_name=='PasswordInput':
            login_pageeles_password_xpath = login_pageele.ele_xpath



    outjsonfile = None
    outloginurl = "%s%s" % (WEB_URL_TITLE,login_modulepage_url)
    outloginaccountxpath = login_pageeles_account_xpath
    outloginaccounttext = None
    outloginppasswordxpath = login_pageeles_password_xpath
    outloginpasswordtext = None
    outloginbuttonxpath = None

    getcookie = GetCookie(outjsonfile = outjsonfile, outloginurl = outloginurl, outloginaccountxpath = outloginaccountxpath,
    outloginaccounttext = outloginaccounttext, outloginppasswordxpath = outloginppasswordxpath, outloginpasswordtext = outloginpasswordtext,
    outloginbuttonxpath = outloginbuttonxpath)   #实例化
    getcookie.writerCookieToJson()









