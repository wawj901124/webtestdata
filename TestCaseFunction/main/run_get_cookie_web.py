# ----------------------------------------------------------------------
import os, django,sys
pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import time

from base.getcookie import GetCookie


class GetCookieSleep:

    def getcookiesleep(self):
        while True:
            try:
                print("线程获取cookie启动")

                from pageelement.models import PageEle, ModulePage
                from webtestdata.settings import WEB_URL_TITLE

                testproject = u"印尼钱包商户管理平台"
                testmodule = u"账号登录"
                testpage = u"login"

                login_modulepages = ModulePage.objects.filter(testproject__web_project=testproject).filter(
                    projectmodule__web_module=testmodule).filter(ele_page=testpage)

                for login_modulepage in login_modulepages:
                    login_modulepage_url = login_modulepage.ele_page_url
                    login_modulepage_id = login_modulepage.id

                login_pageeles = PageEle.objects.filter(modulepage_id=login_modulepage_id)
                for login_pageele in login_pageeles:
                    if login_pageele.ele_name == 'AccountInput':
                        login_pageeles_account_xpath = login_pageele.ele_xpath
                    if login_pageele.ele_name == 'PasswordInput':
                        login_pageeles_password_xpath = login_pageele.ele_xpath

                outjsonfile = None
                outloginurl = "%s%s" % (WEB_URL_TITLE, login_modulepage_url)
                outloginaccountxpath = login_pageeles_account_xpath
                outloginaccounttext = None
                outloginppasswordxpath = login_pageeles_password_xpath
                outloginpasswordtext = None
                outloginbuttonxpath = None

                getcookie = GetCookie(outjsonfile=outjsonfile, outloginurl=outloginurl,
                                      outloginaccountxpath=outloginaccountxpath,
                                      outloginaccounttext=outloginaccounttext,
                                      outloginppasswordxpath=outloginppasswordxpath,
                                      outloginpasswordtext=outloginpasswordtext,
                                      outloginbuttonxpath=outloginbuttonxpath)  # 实例化
                getcookie.writerCookieToJson()

                print("线程获取cookie结束")
                print("等待1200秒")
                time.sleep(1200)
            except Exception as e:
                print("出现异常,异常原因：%s" % e)
            finally:
                True


if __name__ == '__main__':
    starttime = time.time()
    print("开始时间：%s" % starttime)
    gcs = GetCookieSleep()
    gcs.getcookiesleep()



