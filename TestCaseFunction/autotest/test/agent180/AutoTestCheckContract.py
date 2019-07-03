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
from autotest.config.page.agent180.checkContractPage import MerchantContractPage

checkcontract = MerchantContractPage()

testpagebankaccount = checkcontract.bankaccount   #---Bank account---#
testpagebankaccounttext = checkcontract.bankaccounttext
testpagemerchantname = checkcontract.merchantname
testpagemerchantnametext = checkcontract.merchantnametext
testpagemerchantid = checkcontract.merchantid
testpagemerchantidtext = checkcontract.merchantidtext

testpagesettlement = checkcontract.settlement
testpagesettlementtext = checkcontract.settlementtext
testpagebank = checkcontract.bank
testpagebanktext = checkcontract.banktext
testpageaccountname = checkcontract.accountname
testpageaccountnametext = checkcontract.accountnametext

testpageaccountnumber = checkcontract.accountnumber
testpageaccountnumbertext = checkcontract.accountnumbertext
testpagemerchantnamevalue = checkcontract.merchantnamevalue
testpagemerchantnamevaluetext = checkcontract.merchantnamevaluetext
testpagemerchantidvalue = checkcontract.merchantidvalue
testpagemerchantidvaluetext = checkcontract.merchantidvaluetext

testpagebankvalue = checkcontract.bankvalue
testpagebankvaluetext = checkcontract.bankvaluetext
testpageaccountnamevalue= checkcontract.accountnamevalue
testpageaccountnamevaluetext = checkcontract.accountnamevaluetext
testpageaccountnumbervalue = checkcontract.accountnumbervalue
testpageaccountnumbervaluetext = checkcontract.accountnumbervaluetext

testpagempfoffinecollect = checkcontract.mpfoffinecollect       #---MPF-offine collect---#
testpagempfoffinecollecttext = checkcontract.mpfoffinecollecttext
testpageminimumidr = checkcontract.minimumidr
testpageminimumidrtext = checkcontract.minimumidrtext
testpagesettlecycle = checkcontract.settlecycle
testpagesettlecycletext = checkcontract.settlecycletext

testpagerefundsetting = checkcontract.refundsetting
testpagerefundsettingtext = checkcontract.refundsettingtext
testpagempfsettings = checkcontract.mpfsettings
testpagempfsettingstext = checkcontract.mpfsettingstext
testpagempfladder = checkcontract.mpfladder
testpagempfladdertext = checkcontract.mpfladdertext

testpagempfladderfixed = checkcontract.mpfladderfixed
testpagempfladderfixedtext = checkcontract.mpfladderfixedtext
testpagempfladderfeepercent = checkcontract.mpfladderfeepercent
testpagempfladderfeepercenttext = checkcontract.mpfladderfeepercenttext
testpagempfladdefeeminimum = checkcontract.mpfladdefeeminimum
testpagempfladdefeeminimumtext = checkcontract.mpfladdefeeminimumtext

testpageminimumidrvalue = checkcontract.minimumidrvalue
testpageminimumidrvaluetext = checkcontract.minimumidrvaluetext
testpagesettlecyclevalue = checkcontract.settlecyclevalue
testpagesettlecyclevaluetext = checkcontract.settlecyclevaluetext
testpagerefundsettingvalue = checkcontract.refundsettingvalue
testpagerefundsettingvaluetext = checkcontract.refundsettingvaluetext

testpagempfsettingsvalue = checkcontract.mpfsettingsvalue
testpagempfsettingsvaluetext = checkcontract.mpfsettingsvaluetext
testpagempfladderfixedvalue  = checkcontract.mpfladderfixedvalue
testpagempfladderfixedvaluetext = checkcontract.mpfladderfixedvaluetext
testpagempfladderfeepercentvalue = checkcontract.mpfladderfeepercentvalue
testpagempfladderfeepercentvaluetext = checkcontract.mpfladderfeepercentvaluetext

testpagempfladdefeeminimumvalue = checkcontract.mpfladdefeeminimumvalue
testpagempfladdefeeminimumvaluetext = checkcontract.mpfladdefeeminimumvaluetext


testdata = (
    (testpagebankaccount, testpagebankaccounttext),  #---Bank account---#
    (testpagemerchantname, testpagemerchantnametext),
    (testpagemerchantid, testpagemerchantidtext),
    (testpagesettlement, testpagesettlementtext),
    (testpagebank, testpagebanktext),
    (testpageaccountname, testpageaccountnametext),
    (testpageaccountnumber, testpageaccountnumbertext),
    (testpagemerchantnamevalue, testpagemerchantnamevaluetext),
    (testpagemerchantidvalue, testpagemerchantidvaluetext),
    (testpagebankvalue, testpagebankvaluetext),
    (testpageaccountnamevalue, testpageaccountnamevaluetext),
    (testpageaccountnumbervalue, testpageaccountnumbervaluetext),
    (testpagempfoffinecollect, testpagempfoffinecollecttext),  #---MPF-offine collect---#
    (testpageminimumidr, testpageminimumidrtext),
    (testpagesettlecycle, testpagesettlecycletext),
    (testpagerefundsetting, testpagerefundsettingtext),
    (testpagempfsettings, testpagempfsettingstext),
    (testpagempfladder, testpagempfladdertext),
    (testpagempfladderfixed, testpagempfladderfixedtext),
    (testpagempfladderfeepercent, testpagempfladderfeepercenttext),
    (testpagempfladdefeeminimum, testpagempfladdefeeminimumtext),
    (testpageminimumidrvalue, testpageminimumidrvaluetext),
    (testpagesettlecyclevalue, testpagesettlecyclevaluetext),
    (testpagerefundsettingvalue, testpagerefundsettingvaluetext),
    (testpagempfsettingsvalue, testpagempfsettingsvaluetext),
    (testpagempfladderfixedvalue, testpagempfladderfixedvaluetext),
    (testpagempfladderfeepercentvalue, testpagempfladderfeepercentvaluetext),
    (testpagempfladdefeeminimumvalue, testpagempfladdefeeminimumvaluetext),
)


class TestCheckContractClass(unittest.TestCase):  # 创建测试类


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
        cls.testpage = MerchantContractPage()
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
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在text:%s"%testtext)

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

        setattr(TestCheckContractClass, 'test_func_%s_%s' % (casenum,testdataone[1]),
                TestCheckContractClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
        i=i+1


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










