import unittest
import json
from webtestdata.settings import WEB_URL_TITLE,AGENT_LOGIN_ACCOUNT,AGENT_LOGIN_PASSWORD


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from APIAutoTest.base.baseFrame import BaseFrame
from APIAutoTest.autotest.config.sanxing.globalconfig import GlobalConfig

global activity_id
global seq
global mer
mer = 10000
class TestApiClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.baseframe = BaseFrame()
        cls.globalconfig = GlobalConfig()
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass

    #定义post请求函数
    def definepost(self,apiurl,json):
        if self.globalconfig.isOnline:
            url = "%s%s"%(self.globalconfig.realmName_Online,apiurl)
        else:
            url = "%s%s"%(self.globalconfig.realmName_Test,apiurl)

        response_text = self.baseframe.post_json(url,json)
        return response_text




    def test_001(self):
        apiurl = "/api/mkt2/act/qr"
        sign_data = "{}"
        global mer
        b_sign_data = self.baseframe.string_to_byte(sign_data)
        if self.globalconfig.isOnline:
            sign = self.baseframe.get_sign_data(b_sign_data,self.globalconfig.private_Rsa_Key_Online)
        else:
            sign = self.baseframe.get_sign_data(b_sign_data,self.globalconfig.private_Rsa_Key_Test)

        json_data = {"mer": mer,
                   "data": '{}',
                   "sign": '%s' % sign,
                   }
        response_text = self.definepost(apiurl,json_data)
        print("response_text:%s"% response_text)
        response_json_data = json.loads(response_text)
        # print("response_json_data:%s" %  response_json_data)
        global activity_id
        global seq
        response_json_data_data= self.baseframe.get_value(response_json_data,"data")
        # print("response_json_data_data:%s"% response_json_data_data)
        response_json_data_data = json.loads(response_json_data_data)
        response_json_data_data_coupons= self.baseframe.get_value(response_json_data_data,"coupons")
        # print("response_json_data_data_coupons:%s"% response_json_data_data_coupons)
        response_json_data_data_coupons_0 = response_json_data_data_coupons[0]
        # print("response_json_data_data_coupons_0 :%s"% response_json_data_data_coupons_0 )
        activity_id = self.baseframe.get_value(response_json_data_data_coupons_0,"activity_id")
        seq = self.baseframe.get_value(response_json_data_data_coupons_0,"seq")
        print("activity_id :%s"% activity_id )
        print("seq :%s"% seq)




    def test_002(self):
        global activity_id
        global seq
        print("activity_id :%s"% activity_id )
        print("seq :%s" % seq)
        apiurl = "/api/mkt2/act/limit"
        data = {"activity_id":activity_id,"seq":seq}
        b_data = self.baseframe.string_to_byte(data)
        s_data = self.baseframe.byte_to_string(b_data)

        if self.globalconfig.isOnline:
            sign = self.baseframe.get_sign_data(b_data,self.globalconfig.private_Rsa_Key_Online)
        else:
            sign = self.baseframe.get_sign_data(b_data,self.globalconfig.private_Rsa_Key_Test)
        global mer
        # 注意：字节加密是一个字节一个字节加密，所以加密的内容要完全一模一样
        json_data = {
            "mer": mer,
            "data": "%s" % s_data,
            "sign": "%s" % sign
        }
        response_text = self.definepost(apiurl,json_data)

#     # def test_002(self):
#     #     self.defineclickandback(self.baseframe.isstartapp)
#     # def test_003(self):
#     #     self.defineclickandback(self.baseframe.isstartapp)
#     # def test_004(self):
#     #     self.defineclickandback(self.baseframe.isstartapp)
#     # def test_005(self):
#     #     self.defineclickandback(self.baseframe.isstartapp)
#     # def test_006(self):
#     #     self.defineclickandback(self.baseframe.isstartapp)
#
#     def defineasserttext(self,text,pretext):
#         #断言是否存在某个文本
#         testtext = self.baseframe.findbytext_and_return_text(text)
#         self.assertEqual(pretext,testtext)
#         self.baseframe.outPutMyLog("存在text:%s"%testtext)
#
#     def defineasserttextnum(self,num,text,pretext):
#         #断言是否存在某个文本
#         testtext = self.baseframe.findbytext_and_return_text(text)
#         self.assertEqual(pretext,testtext)
#         self.baseframe.outPutMyLog("存在text:%s"%testtext)
#
#
#     @staticmethod    #根据不同的参数生成测试用例(forcount,currentpagetext,nextpagetext,testproject,testmodule,testpage,testcasetitle,starttime):
#     def getTestFunc(forcount,currentpagetext,currrentfindstyle, currentstyleparame,nextpagetext,testproject,testmodule,testpage,testcasetitle,starttime):
#         def func(self):
#             self.defineclickandback(forcount,currentpagetext,currrentfindstyle, currentstyleparame,nextpagetext,testproject,testmodule,testpage,testcasetitle,starttime)
#         return func
#
# def __generateTestCases():
#     # forcount = 10   #获取用例重复次数
#     # for i in range(1, forcount):  # 循环，但去掉第一
#     #     args = []
#     #     args.append(i)
#     #
#     #     setattr(TestIndexClass, 'test_func_%s' % i,
#     #             TestIndexClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
#
#
#     from performancestatistics.models import MeminfoTestCase
#
#     meminfotestcase_all = MeminfoTestCase.objects.filter(testproject="Qrindo").filter(testpage="主页面").order_by('id')
#
#
#     for meminfotestcase in meminfotestcase_all:
#         forcount = meminfotestcase.forcount
#         starttime = GetTimeStr().getTimeStr()
#
#         if len(str(meminfotestcase.id)) == 1:
#             meminfotestcaseid = '0000%s'% meminfotestcase.id
#         elif len(str(meminfotestcase.id)) == 2:
#             meminfotestcaseid = '000%s' % meminfotestcase.id
#         elif len(str(meminfotestcase.id)) == 3:
#             meminfotestcaseid = '00%s' % meminfotestcase.id
#         elif len(str(meminfotestcase.id)) == 4:
#             meminfotestcaseid = '0%s' % meminfotestcase.id
#         elif len(str(meminfotestcase.id)) == 5:
#             meminfotestcaseid = '%s' % meminfotestcase.id
#         else:
#             meminfotestcaseid ='Id已经超过5位数，请重新定义'
#
#         for i in range(1,forcount+1):  # 循环，从1开始
#             if len(str(i)) == 1:
#                 forcount_i = '0000%s' % i
#             elif len(str(i)) == 2:
#                 forcount_i = '000%s' % i
#             elif len(str(i)) == 3:
#                 forcount_i = '00%s' % i
#             elif len(str(i)) == 4:
#                 forcount_i = '0%s' % i
#             elif len(str(i)) == 5:
#                 forcount_i = '%s' % i
#             else:
#                 forcount_i = 'Id已经超过5位数，请重新定义'
#             args = []
#             args.append(i)
#             args.append(meminfotestcase.currentpagetext)
#             args.append(meminfotestcase.currrentfindstyle)
#             args.append(meminfotestcase.currentstyleparame)
#             args.append(meminfotestcase.nextpagetext)
#             args.append(meminfotestcase.testproject)
#             args.append(meminfotestcase.testmodule)
#             args.append(meminfotestcase.testpage)
#             args.append(meminfotestcase.testcasetitle)
#             args.append(starttime)
#
#             setattr(TestIndexClass, 'test_func_%s_%s_%s' % (meminfotestcaseid,meminfotestcase.testcasetitle,forcount_i),
#                     TestIndexClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
#
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










