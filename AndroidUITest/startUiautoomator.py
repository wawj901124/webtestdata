import os
import datetime


class StartUiautomator(object):
    # 使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()和DumpRead()
    def excuOrder(self,orderName):
        check = os.popen(orderName)
        c = check.read()
        print("执行命令：%s" % orderName)
        print("执行命令后返回的内容：%s" % c)
        check.close()
        return c

    #获取时间字符串
    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        # print("当前时间：%s"% now_time)
        # print("时间串：%s"% timestr)
        return timestr

    def uiautomatorInit(self,pythonevn):
        cmdorder = "%s\python -m uiautomator2 init"%pythonevn
        self.excuOrder(cmdorder)
        cmdorder2 = "%s\python -m weditor"%pythonevn
        self.excuOrder(cmdorder2)




if __name__=="__main__":
    pyevn = "D:\djangoworkon\webtest\Scripts"
    su = StartUiautomator()
    su.uiautomatorInit(pyevn)


