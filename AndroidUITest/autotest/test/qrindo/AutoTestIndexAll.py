import unittest

from webtestdata.settings import WEB_URL_TITLE,AGENT_LOGIN_ACCOUNT,AGENT_LOGIN_PASSWORD


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from AndroidUITest.base.baseFrame import BaseFrame
from AndroidUITest.autotest.config.page.qrindo.indexPage import IndexPage
from AndroidUITest.base.performanceFrame import PerformanceFrame
from AndroidUITest.autotest.config.page.qrindo.myQrCodePage import MyQrCodePage
from AndroidUITest.util.gettimestr import GetTimeStr
from AndroidUITest.autotest.config.page.qrindo.loginWithOTP import loginwithotppage_commonfunction
from AndroidUITest.autotest.config.page.qrindo.loginWithPasswordPage import loginwithpasswordpage_commonfunction
from AndroidUITest.autotest.config.page.qrindo.globalConfig import globalconfig



class TestIndexClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.devicename = globalconfig.devicename
        cls.appversion = globalconfig.appversion
        cls.apppackagename = globalconfig.apppackagename
        cls.baseframe = BaseFrame(outdevice=cls.devicename,apppacakagename=cls.apppackagename)
        cls.d = cls.baseframe.d
        cls.indexpage = IndexPage()
        cls.performanceframe = PerformanceFrame()
        cls.myqrcodepage = MyQrCodePage()
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass

    #定义登录函数
    def definelogin(self):
        loginwithotppage_commonfunction.define_click_loginwithpassword_function(self.baseframe)
        if globalconfig.isOnline:
            loginwithpasswordpage_commonfunction.define_login_function(self.baseframe, globalconfig.online_account,
                                                                       globalconfig.online_password)
        else:
            loginwithpasswordpage_commonfunction.define_login_function(self.baseframe, globalconfig.test_account,
                                                                       globalconfig.test_password)

    #定义搜索查找函数
    def defineclickandback(self,forcount,currentpagetext,currrentfindstyle, currentstyleparame,nextpagetext,testproject,testmodule,testpage,testcasetitle,starttime):
        if forcount == 1:
            isstartapp = True
        else:
            isstartapp =self.baseframe.isstartapp

        if isstartapp==True:
            #启动应用
            self.baseframe.startapp()
            self.baseframe.delaytime(5)
            Login_isExist = loginwithotppage_commonfunction.define_is_loginwithpassword_exist_function(self.baseframe)
            # print("Login_isExist:%s" % Login_isExist)
            if Login_isExist:
                self.definelogin()

        meminfoarray = []
        #———————————————第一次获取内存———————————————————————————————
        # 获取当前页面占用内存
        hs10 = self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename, self.appversion, self.apppackagename)
        meminfoarray.append(hs10)
        #延时10秒
        self.baseframe.delaytime(10)
        # 找到该页面的某个元素
        self.defineasserttext(currentpagetext,currentpagetext)
        #———————————————静置10秒后，第二次获取内存———————————————————————————————
        #获取当前页面占用内存
        hs1 = self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename,self.appversion,self.apppackagename)
        meminfoarray.append(hs1)
        #点击元素
        self.baseframe.findelement_and_click(currrentfindstyle,currentstyleparame)
        #———————————————进入下一个页面，第三次获取内存———————————————————————————————
        #获取当前页面占用内存
        hs20=self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename,self.appversion,self.apppackagename)
        meminfoarray.append(hs20)
        self.baseframe.delaytime(10)
        if not self.baseframe.ele_is_exist("text",nextpagetext):
            self.baseframe.outPutMyLog("页面元素还未加载出来，再次进行10秒等待。")
            self.baseframe.delaytime(10)
        #找到该页面的某个元素
        # self.baseframe.findbytext(self.myqrcodepage.balance_text)
        self.defineasserttext(nextpagetext,nextpagetext)
        #———————————————静置10秒后，第四次获取内存———————————————————————————————
        #获取当前页面占用内存
        hs21=self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename,self.appversion,self.apppackagename)
        meminfoarray.append(hs21)
        self.baseframe.delaytime(10)
        #———————————————静置10秒后，第五次获取内存———————————————————————————————
        #获取当前页面占用内存
        hs2=self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename,self.appversion,self.apppackagename)
        meminfoarray.append(hs2)
        #点击返回按钮
        self.baseframe.clickback()
        # self.baseframe.findbyresourceId_and_click(self.myqrcodepage.back_resourceId)
        #———————————————点击返回，第六次获取内存———————————————————————————————
        #获取当前页面占用内存
        hs30 = self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename,self.appversion,self.apppackagename)
        meminfoarray.append(hs30)
        self.baseframe.delaytime(10)
        # 找到该页面的某个元素
        self.defineasserttext(currentpagetext, currentpagetext)
        #———————————————静置10秒后，第七次获取内存———————————————————————————————
        #获取当前页面占用内存
        hs31 = self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename,self.appversion,self.apppackagename)
        meminfoarray.append(hs31)
        self.baseframe.delaytime(10)
        #———————————————静置10秒后，第八次获取内存———————————————————————————————
        #获取当前页面占用内存
        hs3 = self.performanceframe.getCurrentPageMeninfoHeapAll(self.devicename,self.appversion,self.apppackagename)
        meminfoarray.append(hs3)
        self.baseframe.outPutMyLog("当前页内存：%s KB,静置10秒后，内存：%s KB,点击进入下一个页面内存：%s KB,静置10秒后，内存：%s KB,静置10秒后，内存：%s KB,点击返回后内存：%s,静置10秒后，内存：%s,静置10秒后，内存：%s" % (hs10,hs1,hs20,hs21,hs2,hs30,hs31,hs3))
        self.baseframe.outPutMyLog("meminfoarray:%s" % meminfoarray)
        from performancestatistics.models import MeminfoTestResult
        meminfotestresult = MeminfoTestResult()
        meminfotestresult.testproject = testproject
        meminfotestresult.testmodule = testmodule
        meminfotestresult.testpage =testpage
        meminfotestresult.testcasetitle = testcasetitle
        meminfotestresult.teststarttime = starttime
        meminfotestresult.forcount = forcount
        meminfotestresult.currentpagepsstotal = hs10[0]
        meminfotestresult.currentpageheapsize = hs10[1]
        meminfotestresult.currentpageheapalloc = hs10[2]
        meminfotestresult.currentpageheapfree = hs10[3]
        meminfotestresult.currentpageobjectsviews = hs10[4]
        meminfotestresult.currentpageobjectsactivities = hs10[5]

        meminfotestresult.currentpageaftertenpsstotal = hs1[0]
        meminfotestresult.currentpageaftertenheapsize = hs1[1]
        meminfotestresult.currentpageaftertenheapalloc = hs1[2]
        meminfotestresult.currentpageaftertenheapfree = hs1[3]
        meminfotestresult.currentpageaftertenobjectsviews = hs1[4]
        meminfotestresult.currentpageaftertenobjectsactivities = hs1[5]

        meminfotestresult.clicknextpagepsstotal = hs20[0]
        meminfotestresult.clicknextpageheapsize = hs20[1]
        meminfotestresult.clicknextpageheapalloc = hs20[2]
        meminfotestresult.clicknextpageheapfree = hs20[3]
        meminfotestresult.clicknextpageobjectsviews = hs20[4]
        meminfotestresult.clicknextpageobjectsactivities = hs20[5]

        meminfotestresult.nextaftertenpsstotal = hs21[0]
        meminfotestresult.nextaftertenheapsize = hs21[1]
        meminfotestresult.nextaftertenheapalloc = hs21[2]
        meminfotestresult.nextaftertenheapfree = hs21[3]
        meminfotestresult.nextaftertenobjectsviews = hs21[4]
        meminfotestresult.nextaftertenobjectsactivities = hs21[5]

        meminfotestresult.nextaftertentwopsstotal = hs2[0]
        meminfotestresult.nextaftertentwoheapsize = hs2[1]
        meminfotestresult.nextaftertentwoheapalloc = hs2[2]
        meminfotestresult.nextaftertentwoheapfree = hs2[3]
        meminfotestresult.nextaftertentwoobjectsviews = hs2[4]
        meminfotestresult.nextaftertentwoobjectsactivities = hs2[5]

        meminfotestresult.clickbackpsstotal = hs30[0]
        meminfotestresult.clickbackheapsize = hs30[1]
        meminfotestresult.clickbackheapalloc = hs30[2]
        meminfotestresult.clickbackheapfree = hs30[3]
        meminfotestresult.clickbackobjectsviews = hs30[4]
        meminfotestresult.clickbackobjectsactivities = hs30[5]

        meminfotestresult.backaftertenpsstotal = hs31[0]
        meminfotestresult.backaftertenheapsize = hs31[1]
        meminfotestresult.backaftertenheapalloc = hs31[2]
        meminfotestresult.backaftertenheapfree = hs31[3]
        meminfotestresult.backaftertenobjectsviews = hs31[4]
        meminfotestresult.backaftertenobjectsactivities = hs31[5]

        meminfotestresult.backaftertentwopsstotal = hs3[0]
        meminfotestresult.backaftertentwoheapsize = hs3[1]
        meminfotestresult.backaftertentwoheapalloc = hs3[2]
        meminfotestresult.backaftertentwoheapfree = hs3[3]
        meminfotestresult.backaftertentwoobjectsviews = hs3[4]
        meminfotestresult.backaftertentwoobjectsactivities = hs3[5]

        meminfotestresult.test_phone_name = self.devicename
        meminfotestresult.test_app_packagename = self.apppackagename
        meminfotestresult.test_app_version = self.appversion
        meminfotestresult.save()
        return meminfoarray

    # def test_001(self):
    #     self.definelogin()
    # def test_002(self):
    #     self.defineclickandback(3)
    # def test_002(self):
    #     self.defineclickandback(self.baseframe.isstartapp)
    # def test_003(self):
    #     self.defineclickandback(self.baseframe.isstartapp)
    # def test_004(self):
    #     self.defineclickandback(self.baseframe.isstartapp)
    # def test_005(self):
    #     self.defineclickandback(self.baseframe.isstartapp)
    # def test_006(self):
    #     self.defineclickandback(self.baseframe.isstartapp)

    def defineasserttext(self,text,pretext):
        #断言是否存在某个文本
        testtext = self.baseframe.findbytext_and_return_text(text)
        self.assertEqual(pretext,testtext)
        self.baseframe.outPutMyLog("存在text:%s"%testtext)

    def defineasserttextnum(self,num,text,pretext):
        #断言是否存在某个文本
        testtext = self.baseframe.findbytext_and_return_text(text)
        self.assertEqual(pretext,testtext)
        self.baseframe.outPutMyLog("存在text:%s"%testtext)


    @staticmethod    #根据不同的参数生成测试用例(forcount,currentpagetext,nextpagetext,testproject,testmodule,testpage,testcasetitle,starttime):
    def getTestFunc(forcount,currentpagetext,currrentfindstyle, currentstyleparame,nextpagetext,testproject,testmodule,testpage,testcasetitle,starttime):
        def func(self):
            self.defineclickandback(forcount,currentpagetext,currrentfindstyle, currentstyleparame,nextpagetext,testproject,testmodule,testpage,testcasetitle,starttime)
        return func

def __generateTestCases():
    # forcount = 10   #获取用例重复次数
    # for i in range(1, forcount):  # 循环，但去掉第一
    #     args = []
    #     args.append(i)
    #
    #     setattr(TestIndexClass, 'test_func_%s' % i,
    #             TestIndexClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


    from performancestatistics.models import MeminfoTestCase

    meminfotestcase_all = MeminfoTestCase.objects.filter(testproject="Qrindo").filter(testpage="主页面").filter(id=8).order_by('id')


    for meminfotestcase in meminfotestcase_all:
        forcount = meminfotestcase.forcount
        starttime = GetTimeStr().getTimeStr()

        if len(str(meminfotestcase.id)) == 1:
            meminfotestcaseid = '0000%s'% meminfotestcase.id
        elif len(str(meminfotestcase.id)) == 2:
            meminfotestcaseid = '000%s' % meminfotestcase.id
        elif len(str(meminfotestcase.id)) == 3:
            meminfotestcaseid = '00%s' % meminfotestcase.id
        elif len(str(meminfotestcase.id)) == 4:
            meminfotestcaseid = '0%s' % meminfotestcase.id
        elif len(str(meminfotestcase.id)) == 5:
            meminfotestcaseid = '%s' % meminfotestcase.id
        else:
            meminfotestcaseid ='Id已经超过5位数，请重新定义'

        for i in range(1,forcount+1):  # 循环，从1开始
            if len(str(i)) == 1:
                forcount_i = '0000%s' % i
            elif len(str(i)) == 2:
                forcount_i = '000%s' % i
            elif len(str(i)) == 3:
                forcount_i = '00%s' % i
            elif len(str(i)) == 4:
                forcount_i = '0%s' % i
            elif len(str(i)) == 5:
                forcount_i = '%s' % i
            else:
                forcount_i = 'Id已经超过5位数，请重新定义'
            args = []
            args.append(i)
            args.append(meminfotestcase.currentpagetext)
            args.append(meminfotestcase.currrentfindstyle)
            args.append(meminfotestcase.currentstyleparame)
            args.append(meminfotestcase.nextpagetext)
            args.append(meminfotestcase.testproject)
            args.append(meminfotestcase.testmodule)
            args.append(meminfotestcase.testpage)
            args.append(meminfotestcase.testcasetitle)
            args.append(starttime)

            setattr(TestIndexClass, 'test_func_%s_%s_%s' % (meminfotestcaseid,meminfotestcase.testcasetitle,forcount_i),
                    TestIndexClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


    # file_name = "D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\dataconfig\\assertselectsearchmanager.xls"
    # sheet_id = 0
    # datasheet = GetData(file_name,sheet_id)   #实例化
    # # rows_count = datasheet.get_case_lines()   #获取表的行数
    # for i in range(1, rows_count):  # 循环，但去掉第一
    #     args = []
    #     args.append(i)
    #     args.append(datasheet.is_cookie(i))
    #     args.append(datasheet.get_url(i))
    #     args.append(datasheet.get_selectxpath(i))
    #     args.append(datasheet.get_selectoptiontext(i))
    #     args.append(datasheet.get_selectinputxpath(i))
    #     args.append(datasheet.get_selectinputtext(i))
    #     args.append(datasheet.get_searchbuttonxpath(i))
    #     args.append(datasheet.get_searchtableresultxpath(i))
    #     args.append(datasheet.get_colnum(i))
    #     args.append(datasheet.get_checktext(i))
    #
    #
    #     setattr(TestSearchClass, 'test_func_%s_%s' % (datasheet.get_id(i),datasheet.get_title(i)),
    #             TestSearchClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










