import unittest

from webtestdata.settings import WEB_URL_TITLE,MANAGER_LOGIN_ACCOUNT,MANAGER_LOGIN_PASSWORD,MARKETING_CREATE_ACTIVITYID

from webtestdata.settings import RW_DSX_EDIT_ACTIVITYID,RW_JXZ_EDIT_ACTIVITYID,RW_YJS_EDIT_ACTIVITYID   #导入任务活动ID
from webtestdata.settings import YY_DSX_EDIT_ACTIVITYID,YY_JXZ_EDIT_ACTIVITYID,YY_YJS_EDIT_ACTIVITYID   #导入运营活动ID


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson
from TestCaseFunction.util.gettimestr import GetTimeStr

from TestCaseFunction.autotest.config.page.manager.loginPage import LoginPage   #导入登录页





class TestCreateStatusCheckClass(unittest.TestCase):  # 创建测试类


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





        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    def writexunicookie(self):
        addcookie = {'name': '.nereus.manager.settle.banks', 'value': 'QCK9GvKG8OEOh6lRUyyLlmKnHl8i3w'}
        self.activeweb.driver.add_cookie(addcookie)
        self.activeweb.driver.refresh()
        self.activeweb.delayTime(5)
        self.activeweb.outPutMyLog("写入虚拟银行cookie完成")

    #定义创建活动,
    #投放渠道一级为1表示内部渠道，为2表示外部渠道
    #投放渠道二级为0表示全选，为1，2，等表示选一项和选多项组合，程序中只有全选和选择一项的情况
    # 任务类型为1表示注册，为2表示交易类型
    #奖励类型1表示固定奖励
    def definestatuscheck(self,num,
                          firsturl,secondurl,
                             isstatus,istype,type):
        #加载一个待上线的运营活动编辑页路径
        # firsturl = "https://bjw.halodigit.com:9060/nereus/marketing/admin/v/#/activityManage/missionAct/modifyOnLine/%s"
        self.activeweb.getUrl(firsturl)
        self.activeweb.delayTime(6)

        #加载一个进行中的运营活动的ID
        # secondurl = "https://bjw.halodigit.com:9060/nereus/marketing/admin/v/#/activityManage/missionAct/modifyOnLine/%s"

        self.activeweb.getUrl(secondurl)
        self.activeweb.delayTime(8)

        if isstatus:
            #断言处于活动列表页

            realurl = self.activeweb.getNowPageUrl()
            if type == "1":
                perurl = "%s/nereus/marketing/admin/v/#/activityManage/missionAct/list"% WEB_URL_TITLE
            elif type == "2":
                perurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/list" % WEB_URL_TITLE
            self.assertEqual(perurl,realurl)
        if istype:
            #断言出现参数错误弹框
            realtankuangtext = self.activeweb.findElementByXpathAndReturnText(num,"/html/body/div[5]/div[2]/div/div/div/div/div[2]/div")
            pretankuangtext = "Params invalid"
            self.assertEqual(pretankuangtext, realtankuangtext)




    #编辑页测试
    # @unittest.skip('test0001')
    def test0001(self):
        """
        测试在运营活动待上线活动编辑页，加载运营活动进行中的活动的ID，到达运营活动列表页
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,YY_JXZ_EDIT_ACTIVITYID)

        self.definestatuscheck("test0001",firsturl,secondurl,True,False,"2")

    # @unittest.skip('test0002')
    def test0002(self):
        """
        测试在运营活动待上线活动编辑页，加载运营活动已结束的活动的ID，到达运营活动列表页
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,YY_YJS_EDIT_ACTIVITYID)

        self.definestatuscheck("test0002",firsturl,secondurl,True,False,"2")

    # @unittest.skip('test0003')
    def test0003(self):
        """
        测试在运营活动进行中的活动编辑页，加载运营活动待上线的活动的ID，到达运营活动列表页
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,YY_JXZ_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)

        self.definestatuscheck("test0003",firsturl,secondurl,True,False,"2")

    # @unittest.skip('test0005')
    def test0005(self):
        """
        测试在运营活动进行中的活动编辑页，加载运营活动已结束的活动的ID，到达运营活动列表页
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,YY_JXZ_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,YY_YJS_EDIT_ACTIVITYID)

        self.definestatuscheck("test0005",firsturl,secondurl,True,False,"2")

    # @unittest.skip('test0006')
    def test0006(self):
        """
        测试在运营活动待上线的活动编辑页，加载任务活动待上线的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,RW_DSX_EDIT_ACTIVITYID)

        self.definestatuscheck("test0006",firsturl,secondurl,False,True,"2")

    # @unittest.skip('test0007')
    def test0007(self):
        """
        测试在运营活动待上线的活动编辑页，加载任务活动进行中的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,RW_JXZ_EDIT_ACTIVITYID)

        self.definestatuscheck("test0007",firsturl,secondurl,False,True,"2")

    # @unittest.skip('test0008')
    def test0008(self):
        """
        测试在运营活动待上线的活动编辑页，加载任务活动已结束的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOnLine/%s"%(WEB_URL_TITLE,RW_YJS_EDIT_ACTIVITYID)

        self.definestatuscheck("test0008",firsturl,secondurl,False,True,"2")

    # @unittest.skip('test0009')
    def test0009(self):
        """
        测试在运营活动进行中的活动编辑页，加载任务活动待上线的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,YY_JXZ_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,RW_DSX_EDIT_ACTIVITYID)

        self.definestatuscheck("test0009",firsturl,secondurl,False,True,"2")

    # @unittest.skip('test0010')
    def test0010(self):
        """
        测试在运营活动进行中的活动编辑页，加载任务活动进行中的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,YY_JXZ_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,RW_JXZ_EDIT_ACTIVITYID)

        self.definestatuscheck("test0010",firsturl,secondurl,False,True,"2")

    # @unittest.skip('test0011')
    def test0011(self):
        """
        测试在运营活动进行中的活动编辑页，加载任务活动已结束的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,YY_JXZ_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s"%(WEB_URL_TITLE,RW_YJS_EDIT_ACTIVITYID)

        self.definestatuscheck("test0011",firsturl,secondurl,False,True,"2")

    #详情页测试
    # @unittest.skip('test0012')
    def test0012(self):
        """
        测试在运营活动待上线的活动详情页，加载任务活动待上线的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/operationDetail/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/operationDetail/%s"%(WEB_URL_TITLE,RW_DSX_EDIT_ACTIVITYID)

        self.definestatuscheck("test0012",firsturl,secondurl,False,True,"2")

    # @unittest.skip('test0013')
    def test0013(self):
        """
        测试在运营活动待上线的活动详情页，加载任务活动进行中的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/operationDetail/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/operationDetail/%s"%(WEB_URL_TITLE,RW_JXZ_EDIT_ACTIVITYID)

        self.definestatuscheck("test0013",firsturl,secondurl,False,True,"2")

    # @unittest.skip('test0014')
    def test0014(self):
        """
        测试在运营活动待上线的活动详情页，加载任务活动已结束的活动的ID，出现参数错误弹框
        :return:
        """
        firsturl = "%s/nereus/marketing/admin/v/#/activityManage/operation/operationDetail/%s"%(WEB_URL_TITLE,YY_DSX_EDIT_ACTIVITYID)
        secondurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/operationDetail/%s"%(WEB_URL_TITLE,RW_YJS_EDIT_ACTIVITYID)

        self.definestatuscheck("test0014",firsturl,secondurl,False,True,"2")




#
#
#
#
#
#     def defineasserttextnum(self,num,testelexpath,expecttext):
#         #断言是否存在某个文本
#         testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
#         self.assertEqual(expecttext,testtext)
#         self.activeweb.outPutMyLog("存在text:%s"%testtext)
#
#     def defineisintable(self,num,testtablexpath,expecttext,tablecolnum):
#         notexsitflag = True
#         tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, testtablexpath)
#         for value in tabledic.values():
#             # self.activeweb.outPutMyLog("%s"% value[int(tablecolnum)])
#             if str(expecttext).lower() in value[int(tablecolnum)].lower():
#                 self.assertTrue(True)
#                 self.activeweb.outPutMyLog("在【%s】中存在:【%s】"% (value[int(tablecolnum)],expecttext))
#                 notexsitflag = False
#                 break
#         if notexsitflag:
#             self.activeweb.outPutMyLog("在【%s】不存在：【%s】"% (tabledic,expecttext))
#             self.assertTrue(False)
#
#
#
#     @staticmethod    #根据不同的参数生成测试用例
#     def getTestFunc(num,hdmcinputtext,hdysinputtext,
#                     tfqdyj, tfqdej,hdbztextareainputtext,
#                     rwlx,tjrwxz,
#                     jyjylx, jyzffs,
#                     jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
#                     jllx,iscancel):
#         def func(self):
#             self.definecreateactivity(num,
#                              hdmcinputtext,hdysinputtext,
#                              tfqdyj, tfqdej,hdbztextareainputtext,
#                              rwlx,tjrwxz,
#                              jyjylx, jyzffs,
#                              jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
#                              jllx,iscancel)
#         return func
#
# def __generateTestCases():
#     from addactivity.models import AddActivity
#
#     addactivity_all = AddActivity.objects.filter(testproject="营销系统").filter(testmodule="任务活动管理").filter(testpage="创建活动").filter(id=1).order_by('id')
#     rows_count = addactivity_all.count()
#
#     for addactivity in addactivity_all:
#
#         if len(str(addactivity.id)) == 1:
#             addactivityid = '0000%s'% addactivity.id
#         elif len(str(addactivity.id)) == 2:
#             addactivityid = '000%s' % addactivity.id
#         elif len(str(addactivity.id)) == 3:
#             addactivityid = '00%s' % addactivity.id
#         elif len(str(addactivity.id)) == 4:
#             addactivityid = '0%s' % addactivity.id
#         elif len(str(addactivity.id)) == 5:
#             addactivityid = '%s' % addactivity.id
#         else:
#             addactivityid ='Id已经超过5位数，请重新定义'
#
#
#         args = []
#         args.append(addactivity.id)
#         args.append("%s_%s"%(addactivity.hdmcinputtext,GetTimeStr().getTimeStr()))
#         args.append(addactivity.hdysinputtext)
#         args.append(addactivity.tfqdyj)
#         args.append(addactivity.tfqdej)
#         args.append(addactivity.hdbztextareainputtext)
#         args.append(addactivity.rwlx)
#         args.append(addactivity.tjrwxz)
#         args.append(addactivity.jyjylx)
#         args.append(addactivity.jyzffs)
#         args.append(addactivity.jymgyhzdcycsinputtext)
#         args.append(addactivity.jymgyhmrcycsinputtext)
#         args.append(addactivity.jllx)
#         args.append(addactivity.iscancel)
#
#         setattr(TestCreateActivityClass, 'test_func_%s_%s' % (addactivityid,addactivity.testcasetitle),
#                 TestCreateActivityClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
#
#     # file_name = "D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\dataconfig\\assertselectsearchmanager.xls"
#     # sheet_id = 0
#     # datasheet = GetData(file_name,sheet_id)   #实例化
#     # # rows_count = datasheet.get_case_lines()   #获取表的行数
#     # for i in range(1, rows_count):  # 循环，但去掉第一
#     #     args = []
#     #     args.append(i)
#     #     args.append(datasheet.is_cookie(i))
#     #     args.append(datasheet.get_url(i))
#     #     args.append(datasheet.get_selectxpath(i))
#     #     args.append(datasheet.get_selectoptiontext(i))
#     #     args.append(datasheet.get_selectinputxpath(i))
#     #     args.append(datasheet.get_selectinputtext(i))
#     #     args.append(datasheet.get_searchbuttonxpath(i))
#     #     args.append(datasheet.get_searchtableresultxpath(i))
#     #     args.append(datasheet.get_colnum(i))
#     #     args.append(datasheet.get_checktext(i))
#     #
#     #
#     #     setattr(TestSearchClass, 'test_func_%s_%s' % (datasheet.get_id(i),datasheet.get_title(i)),
#     #             TestSearchClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
#
#
# __generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










