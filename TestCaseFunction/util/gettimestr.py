# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/30 17:46'
import datetime
from TestCaseFunction.log.my_log import UserLog

class GetTimeStr:
    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        self.outPutMyLog("当前时间：%s"% now_time)
        self.outPutMyLog("时间串：%s"% timestr)
        # print("当前时间：",now_time)
        # print("时间串：",timestr)
        return timestr

    def outPutMyLog(self,context):
        mylog = UserLog(context)
        mylog.runMyLog()


if __name__  == '__main__':
    gettimestr = GetTimeStr()
    gettimestr.getTimeStr()
