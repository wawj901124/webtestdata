import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


# 在jenkins运行时经常提示找不到包，所以就需要手动添加PYTHONPATH，通过追加sys.path列表来实现
import os
import sys

rootpath = str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
syspath = sys.path
sys.path = []
sys.path.append(rootpath)  # 将工程根目录加入到python搜索路径中
sys.path.extend([rootpath + i for i in os.listdir(rootpath) if i[0] != "."])  # 将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
# 追加完成


from TestCaseFunction.htmltest import HTMLTestRunner_jietuxiugai_aboutmysql as HTMLTestRunner
from test import *
from TestCaseFunction.test.alltest_list_aboutmysql import caselist  #调用数组文件
from TestCaseFunction.util.gettimestr import GetTimeStr
from TestCaseFunction.util.send_attach_email import SendEmail

from TestCaseFunction.log.my_log import UserLog



class RunAllTest(unittest.TestCase):

    def runAllTest(self):
        #将用例组件成数组
        alltestnames = caselist()
        suite=unittest.TestSuite()
        for testpy in alltestnames:
            try:
                suite.addTest(unittest.defaultTestLoader.loadTestsFromName(testpy))    #默认加载所有用例
            except Exception:
                print('ERROR: Skipping tests from "%s".' % testpy)
                try:
                    __import__(test)
                except ImportError:
                    print('Could not import the "%s" test module.'% testpy)
                else:
                    print('Could not load the "%s" test suite.' % testpy)
                from traceback import print_exc
                print_exc()
        self.outPutMyLog('Running the tests...')
        # print('Running the tests...')
        gettime = GetTimeStr()
        reporttimestr = gettime.getTimeStr()  #获取当前时间
        currentny = gettime.getTimeStrNY()   #获取当前时间的年月
        reportdir = "%s/media/report/%s" % (str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),currentny)
        gettime.createdir(reportdir)  #创建报告目录
        reportname = "report/%s/%s_report.html" % (currentny,reporttimestr)
        filename = '%s/media/%s' % (str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),reportname)
        fp = open(filename, 'wb')
        self.outPutMyLog('The report path:%s' % filename)

        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'python 自动化测试_测试报告',
            description=u'用例执行情况：',
            verbosity=2)   #verbosity=2,输出测试用例中打印的信息
        runner.run(suite)
        fp.close()

        #保存报告到数据库
        from reportrecord.models import Report
        reportrd = Report()  # 数据库的对象等于Report,实例化
        reportrd.reportname = reporttimestr
        print(reportname)
        reportrd.reportfile = reportname
        reportrd.save()

        # 发送report至邮箱
        send_e = SendEmail()
        send_e.send_main([1], [2], filename)

    def outPutMyLog(self, context):
        mylog = UserLog(context)
        mylog.runMyLog()

    def run(self):
        self.outPutMyLog('---------------------------')
        # print('---------------------------')
        stdout_backup = sys.stdout
        gettime = GetTimeStr()
        timestr = gettime.getTimeStr()
        # define the log file that receives your log info
        logpath = "%s/log/%s_message.txt" % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),timestr)
        log_file = open(logpath, "w", encoding="utf-8")
        self.outPutMyLog('Now all print info will be written to message.log')
        # print("Now all print info will be written to message.log")
        # redirect print output to log file
        sys.stdout = log_file
        self.outPutMyLog('----------开始打印日志-----------------\n')
        # print('----------开始打印日志-----------------\n')

        # any command line that you will execute
        self.runAllTest()
        self.outPutMyLog('\n----------日志打印结束-----------------')
        # print('\n----------日志打印结束-----------------')
        log_file.close()
        # restore the output to initial pattern
        sys.stdout = stdout_backup
        self.outPutMyLog('Now this will be presented on screen')
        # print("Now this will be presented on screen")
        # 发送log至邮箱
        send_e = SendEmail()
        send_e.send_main([1], [2], logpath)




if __name__ == '__main__':
    runat = RunAllTest()
    # runat.run()
    runat.runAllTest()






