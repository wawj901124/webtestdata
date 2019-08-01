import os
import datetime
import time

class PerformanceFrame(object):
    # 使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()和DumpRead()
    def excuOrder(self,orderName):
        check = os.popen(orderName)
        c = check.read()
        print("执行命令：%s" % orderName)
        print("执行命令后返回的内容：%s" % c)
        return c

    #获取时间字符串
    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        # print("当前时间：%s"% now_time)
        # print("时间串：%s"% timestr)
        return timestr

    #获取当前存储数据的时间戳
    def getCurrentTime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #  获取当前时间
        return currenttime  #  返回当前时间

    def getCurrentPageMeninfoHeapSize(self,devicename,appversion,apppackagename):
        cmd = 'adb shell "dumpsys meminfo %s | grep TOTAL"' % apppackagename   # 获取cup占用率命令
        content = os.popen(cmd)
        result = content.readlines()
        # print("result:%s"% result)
        alldata = [("deviceid", "appversion", "timestamp", "meminfoheapsize")]  # 要保存的数据，时间戳及cup占用率

        if result != []:
            for line in result:
                # meminfosize = line.split("kB")[0]
                # print("line:%s" % line)
                meminfototal = line.strip()
                # print("meminfototal:%s"% meminfototal)
                meminfosize = meminfototal.split("    ")
                # print("meminfosize:%s"% meminfosize)
                meminfoheapsize = meminfosize[5]
                if meminfoheapsize:   #如果取到值，就终止循环
                    print("获取到内存为：%s kB"% meminfoheapsize)
                    break
            currenttime = self.getCurrentTime()  #  获取当前时间
            alldata.append((devicename,appversion,currenttime,meminfoheapsize))  #  写入数据到self.alldata

            return meminfoheapsize
        else:
            print("没有找到相应APP的信息，请确定APP已经启动运行")
