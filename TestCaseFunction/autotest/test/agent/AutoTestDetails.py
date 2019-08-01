import unittest

from webtestdata.settings import WEB_URL_TITLE,AGENT_LOGIN_ACCOUNT,AGENT_LOGIN_PASSWORD


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

from TestCaseFunction.autotest.config.page.agent.loginPage import LoginPage
from TestCaseFunction.autotest.config.page.agent.detailsPage import DetailsPage

testpage = DetailsPage()


testdata = (
    (testpage.basicinfo, testpage.basicinfotext),  #---Basic info---#
    (testpage.merchantid, testpage.merchantidtext),   #---key---#
    (testpage.loginaccount, testpage.loginaccounttext),
    (testpage.agent, testpage.agenttext),
    (testpage.merchantidvalue, testpage.merchantidvaluetext),   #---value---#
    (testpage.loginaccountvalue, testpage.loginaccountvaluetext),
    (testpage.agentvalue, testpage.agentvaluetext),
    (testpage.merchantinfo, testpage.merchantinfotext),    #---Merchant info---#
    (testpage.brandname, testpage.brandnametext),   #---key---#
    (testpage.email, testpage.emailtext),
    (testpage.contactnumber, testpage.contactnumbertext),
    (testpage.merchanttype, testpage.merchanttypetext),
    (testpage.category, testpage.categorytext),
    (testpage.criteria, testpage.criteriatext),
    (testpage.siup, testpage.siuptext),
    (testpage.province, testpage.provincetext),
    (testpage.city, testpage.citytext),
    (testpage.district, testpage.districttext),
    (testpage.village, testpage.villagetext),
    (testpage.postcode, testpage.postcodetext),
    (testpage.address, testpage.addresstext),
    (testpage.photosiup, testpage.photosiuptext),
    (testpage.photonpwpcompany, testpage.photonpwpcompanytext),
    (testpage.phototdp, testpage.phototdptext),
    (testpage.brandnamevalue, testpage.brandnamevaluetext),    # ---value---#
    (testpage.emailvalue, testpage.emailvaluetext),
    (testpage.contactnumbervalue, testpage.contactnumbervaluetext),
    (testpage.merchanttypevalue, testpage.merchanttypevaluetext),
    (testpage.categoryvalue, testpage.categoryvaluetext),
    (testpage.criteriavalue, testpage.criteriavaluetext),
    (testpage.siupvalue, testpage.siupvaluetext),
    (testpage.provincevalue, testpage.provincevaluetext),
    (testpage.cityvalue, testpage.cityvaluetext),
    (testpage.districtvalue, testpage.districtvaluetext),
    (testpage.villagevalue, testpage.villagevaluetext),
    (testpage.postcodevalue, testpage.postcodevaluetext),
    (testpage.addressvalue, testpage.addressvaluetext),

    (testpage.ownerpersoninchangeinfo, testpage.ownerpersoninchangeinfotext),    #---Owner / Person in Charge info---#
    (testpage.name, testpage.nametext),   # ---key---#
    (testpage.npwp, testpage.npwptext),
    (testpage.typeid, testpage.typeidtext),
    (testpage.identitynumber, testpage.identitynumbertext),
    (testpage.address2, testpage.address2text),
    (testpage.nationality, testpage.nationalitytext),
    (testpage.phone, testpage.phonetext),
    (testpage.email2, testpage.email2text),
    (testpage.photofullfacebust, testpage.photofullfacebusttext),
    (testpage.namevalue, testpage.namevaluetext),  # ---value---#
    (testpage.npwpvalue, testpage.npwpvaluetext),
    (testpage.typeidvalue, testpage.typeidvaluetext),
    (testpage.identitynumbervalue, testpage.identitynumbervaluetext),
    (testpage.address2value, testpage.address2valuetext),
    (testpage.nationalityvalue, testpage.nationalityvaluetext),
    (testpage.phonevalue, testpage.phonevaluetext),
    (testpage.email2value, testpage.email2valuetext),

    (testpage.profilephotos, testpage.profilephotostext),      #---Profile Photos---#
    (testpage.locationphoto, testpage.locationphototext),  # ---key---#
    (testpage.photoofthecashiersdesk, testpage.photoofthecashiersdesktext),
    (testpage.otherphoto, testpage.otherphototext),

)


class TestDetailsClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.activeweb = ActiveWeb()  # 实例化
        cls.loginurl = LoginPage().pageurl
        cls.activeweb.getUrl(cls.loginurl)  # 打开网址
        cls.activeweb.findElementByXpathAndInput(LoginPage().account,AGENT_LOGIN_ACCOUNT)
        cls.activeweb.findElementByXpathAndInput(LoginPage().password,AGENT_LOGIN_PASSWORD)
        cls.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        cls.activeweb.delayTime(3)
        cls.testpage = DetailsPage()
        cls.testpageurl =cls.testpage.pageurl   #测试页面url
        cls.activeweb.getUrl(cls.testpageurl)
        cls.activeweb.delayTime(3)

        # pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        cls.activeweb.closeBrowse()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        # self.activeweb.closeBrowse()
        pass


    def defineasserttextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        clicktext = ["Merchant info","Owner / Person in Charge info","Profile Photos"]
        if  expecttext in clicktext:
            self.activeweb.findElementByXpathAndScriptClickNum(num,testelexpath)
        self.assertEqual(expecttext,testtext)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc( num,testelexpath,expecttext):
        def func(self):
            self.defineasserttextnum(num,testelexpath,expecttext)
        return func

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

        setattr(TestDetailsClass, 'test_func_%s_%s' % (casenum,testdataone[1]),
                TestDetailsClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
        i=i+1


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










