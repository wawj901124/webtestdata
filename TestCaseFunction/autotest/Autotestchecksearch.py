import unittest

from webtestdata.settings import WEB_URL_TITLE


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


# from data.assertselectsearch_get_data import GetData   #导入GetData
from TestCaseFunction.util.send_attach_email import SendEmail
from TestCaseFunction.base.datailfunction import WebFunction
from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson


class TestSearchClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.jsonfile = '../cookiejson/cookiemanager.json'
        self.operationjson = OperationJson(file_path=self.jsonfile)   #实例化
        self.cookie = self.operationjson.get_all_data()
        print("self.cookie:%s" % self.cookie)
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = "https://bjw.halodigit.com:9090/nereus/manager/index#/login"
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    #定义搜索查找函数
    def definesearch(self,num,is_cookie,url,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext):

        if is_cookie:
            self.activeweb.writerCookies(self.cookie, self.loginurl,url)
        else:
            self.activeweb.getUrl(url)

        if selectxpath !=None and selectoptiontext !=None:
            self.activeweb.findElementByXpathAndReturnOptions(selectxpath,str(selectoptiontext))
        if selectinputxpath != None and selectinputtext !=None:
            self.activeweb.findElementByXpathAndInput(selectinputxpath,str(selectinputtext))
        self.activeweb.findElementByXpathAndClick(searchbuttonxpath)
        self.activeweb.delayTime(5)
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num,searchtableresultxpath)
        for value in tabledic.values():
            if str(checktext).lower() in value[int(colnum)].lower():
                self.assertTrue(True)
            else:
                self.assertTrue(False)


    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,is_cookie,url,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext):
        def func(self):
            self.definesearch(num,is_cookie,url,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext)
        return func

def __generateTestCases():
    from testfundata.models import TestSearch

    testsearch_all = TestSearch.objects.all().order_by('id')
    rows_count = testsearch_all.count()

    for testsearch in testsearch_all:
        if testsearch.select_option_xpath == None:
            testsearch_select_option_xpath = None
        else:
            testsearch_select_option_xpath =testsearch.select_option_xpath.ele_xpath

        if testsearch.select_input_xpath == None:
            testsearch_select_input_xpath = None
        else:
            testsearch_select_input_xpath =testsearch.select_input_xpath.ele_xpath
        if len(str(testsearch.id)) == 1:
            testsearchid = '0000%s'%testsearch.id
        elif len(str(testsearch.id)) == 2:
            testsearchid = '000%s' % testsearch.id
        elif len(str(testsearch.id)) == 3:
            testsearchid = '00%s' % testsearch.id
        elif len(str(testsearch.id)) == 4:
            testsearchid = '0%s' % testsearch.id
        elif len(str(testsearch.id)) == 5:
            testsearchid = '%s' % testsearch.id
        else:
            testsearchid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(testsearch.id)
        args.append(testsearch.is_cookie)
        args.append("%s%s" % (WEB_URL_TITLE,testsearch.modulepage.ele_page_url))
        args.append(testsearch_select_option_xpath)
        args.append(testsearch.select_option_text)
        args.append(testsearch_select_input_xpath)
        args.append(testsearch.select_input_text)
        args.append(testsearch.search_button_xpath.ele_xpath)
        args.append(testsearch.search_table_result_xpath.ele_xpath)
        args.append(testsearch.colnum)
        args.append(testsearch.check_text)


        setattr(TestSearchClass, 'test_func_%s_%s_%s_%s_%s' % (testsearchid,testsearch.select_option_xpath,testsearch.select_option_text,testsearch.select_input_xpath,testsearch.select_input_text),
                TestSearchClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










