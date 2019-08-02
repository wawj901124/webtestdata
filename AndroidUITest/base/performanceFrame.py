import os
import datetime
import time

from AndroidUITest.util.my_log import MyLog


class PerformanceFrame(object):
    
    def outPutMyLog(self,context):
        mylog = MyLog(context)
        mylog.runMyLog()
        
    # 使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()和DumpRead()
    def excuOrder(self,orderName):
        check = os.popen(orderName)
        c = check.read()
        self.outPutMyLog("执行命令：%s" % orderName)
        self.outPutMyLog("执行命令后返回的内容：%s" % c)
        return c

    #获取时间字符串
    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        # self.outPutMyLog("当前时间：%s"% now_time)
        # self.outPutMyLog("时间串：%s"% timestr)
        return timestr

    #获取当前存储数据的时间戳
    def getCurrentTime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #  获取当前时间
        return currenttime  #  返回当前时间

    def getCurrentPageMeninfoHeapSize(self,devicename,appversion,apppackagename):
        cmd = 'adb shell "dumpsys meminfo %s | grep TOTAL"' % apppackagename   # 获取cup占用率命令
        content = os.popen(cmd)
        result = content.readlines()
        # self.outPutMyLog("result:%s"% result)
        alldata = [("deviceid", "appversion", "timestamp", "meminfoheapsize")]  # 要保存的数据，时间戳及cup占用率

        if result != []:
            for line in result:
                # meminfosize = line.split("kB")[0]
                # self.outPutMyLog("line:%s" % line)
                meminfototal = line.strip()
                # self.outPutMyLog("meminfototal:%s"% meminfototal)
                meminfosize = meminfototal.split("    ")
                # self.outPutMyLog("meminfosize:%s"% meminfosize)
                meminfoheapsize = meminfosize[5]
                if meminfoheapsize:   #如果取到值，就终止循环
                    self.outPutMyLog("获取到内存为：%s kB"% meminfoheapsize)
                    break
            currenttime = self.getCurrentTime()  #  获取当前时间
            alldata.append((devicename,appversion,currenttime,meminfoheapsize))  #  写入数据到self.alldata

            return meminfoheapsize
        else:
            self.outPutMyLog("没有找到相应APP的信息，请确定APP已经启动运行")
