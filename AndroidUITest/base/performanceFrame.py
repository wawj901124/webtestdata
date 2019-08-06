import os
import datetime
import time

from AndroidUITest.util.my_log import MyLog


class PerformanceFrame(object):
    
    def outPutMyLog(self,context):
        mylog = MyLog(context)
        mylog.runMyLog()

    def outPutErrorMyLog(self,context):
        mylog = MyLog(context)
        mylog.runErrorLog()
        
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
            self.outPutErrorMyLog("没有找到相应APP的信息，请确定APP已经启动运行")


    def getCurrentPageMeninfoHeapAll(self,devicename,appversion,apppackagename):
        cmd = 'adb shell "dumpsys meminfo %s | grep TOTAL"' % apppackagename   # 获取cup占用率命令
        content = os.popen(cmd)
        result = content.readlines()

        cmd_views = 'adb shell "dumpsys meminfo %s | grep Views"' % apppackagename  # 获取cup占用率命令
        content_views = os.popen(cmd_views)
        result_views = content_views.readlines()

        cmd_activities = 'adb shell "dumpsys meminfo %s | grep Activities"' % apppackagename  # 获取cup占用率命令
        content_activities = os.popen(cmd_activities)
        result_activities = content_activities.readlines()


        # self.outPutMyLog("result:%s"% result)
        alldata = [("deviceid", "appversion", "timestamp","psstotal", "meminfoheapsize","meminfoheapalloc","meminfoheapfree","objectsviews","objectsactivities")]  # 要保存的数据，时间戳及cup占用率

        heap = []
        if result != []:
            for line in result:
                # meminfosize = line.split("kB")[0]
                # self.outPutMyLog("line:%s" % line)
                meminfototal = line.strip()
                # self.outPutMyLog("meminfototal:%s"% meminfototal)
                total = meminfototal.split("    ")
                self.outPutMyLog("TOTAL 行:%s"% total)

                if len(total) == 8:
                    psstotal = total[1]
                    meminfoheapsize = total[5]
                    meminfoheapalloc = total[6]
                    meminfoheapfree = total[7]
                    heap.append(psstotal)
                    heap.append(meminfoheapsize)
                    heap.append(meminfoheapalloc)
                    heap.append(meminfoheapfree)

                    self.outPutMyLog("获取到的Pss TOTAL内存为：%s kB"% psstotal)
                    self.outPutMyLog("获取到的Heap Size内存为：%s kB"% meminfoheapsize)
                    self.outPutMyLog("获取到的Heap Alloc内存为：%s kB"% meminfoheapalloc)
                    self.outPutMyLog("获取到的Heap Free内存为：%s kB"% meminfoheapfree)
                elif len(total) == 7:
                    psstotal_mem = total[0]
                    psstotal_mem = psstotal_mem.split("   ")
                    psstotal = psstotal_mem[1]

                    meminfoheapsize = total[4]
                    meminfoheapalloc = total[5]
                    meminfoheapfree = total[6]
                    heap.append(psstotal)
                    heap.append(meminfoheapsize)
                    heap.append(meminfoheapalloc)
                    heap.append(meminfoheapfree)

                    self.outPutMyLog("获取到的Pss TOTAL内存为：%s kB"% psstotal)
                    self.outPutMyLog("获取到的Heap Size内存为：%s kB"% meminfoheapsize)
                    self.outPutMyLog("获取到的Heap Alloc内存为：%s kB"% meminfoheapalloc)
                    self.outPutMyLog("获取到的Heap Free内存为：%s kB"% meminfoheapfree)
                else:
                    self.outPutErrorMyLog("TOTAL 行没有被分成7项或8项！")
                break

            for line_views in result_views:
                line_views_list = line_views.strip()
                line_views_list = line_views_list.split(":")
                line_views = line_views_list[1]
                line_views = line_views.split("         ")
                line_views = line_views[0]
                objectsviews = line_views.strip()
                heap.append(objectsviews)
                self.outPutMyLog("获取到的Objects Views为：%s 个" %  objectsviews)
                break

            for line_activities in result_activities:
                line_activities_list = line_activities.split(":")
                line_activities = line_activities_list[2]
                objectsactivities = line_activities.strip()
                heap.append(objectsactivities)
                self.outPutMyLog("获取到的Objects Activities为：%s 个" % objectsactivities)
                break

            currenttime = self.getCurrentTime()  #  获取当前时间
            alldata.append((devicename,appversion,currenttime,psstotal,meminfoheapsize,meminfoheapalloc,meminfoheapfree,objectsviews,objectsactivities))  #  写入数据到self.alldata
            self.outPutMyLog("获取到的Heap内存为：%s kB" % heap)
            return heap
        else:
            self.outPutErrorMyLog("没有找到相应APP的信息，请确定APP已经启动运行")



    #性能方案网址：https://blog.csdn.net/onfire22/article/details/79679196   https://blog.csdn.net/zouxiongqqq/article/details/83030343



if __name__ == "__main__":
    devicename = "810EBM32TZ4K"
    appversion = "QRindo v1.0.4"
    apppackagename = "com.ahdi.qrindo.wallet"

    pf = PerformanceFrame()
    pf.getCurrentPageMeninfoHeapAll(devicename,appversion,apppackagename)

