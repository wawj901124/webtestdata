# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/9 15:55'
import os
import uiautomator2 as u2
import time
from AndroidUITest.util.gettimestr import GetTimeStr   #导入获取时间串函数
from AndroidUITest.util.my_log import MyLog


class BaseFrame(object):
    def __init__(self,outdevice=None,apppacakagename=None,isusb=None):
        print(outdevice)
        if outdevice==None:
            # self.d = u2.connect('192.168.199.168')
            self.d = u2.connect_usb('192.168.1.100:5555')
        else:
            self.d = u2.connect_usb(outdevice)

        if apppacakagename == None:
            self.packagename = "com.ahdi.qrindo.wallet"
        else:
            self.packagename =apppacakagename
        self.timeStr = GetTimeStr()  # 实例化
        self.isstartapp = False
    
    def outPutMyLog(self,context):
        mylog = MyLog(context)
        mylog.runMyLog()

    def outPutErrorMyLog(self,context):
        mylog = MyLog(context)
        mylog.runErrorLog()


    #执行shell命令
    def adbshell(self,order):
        d = self.d
        d.adb_shell(order)
        self.outPutMyLog('输入shell命令:',order,'。\n')


    #启动app
    def startapp(self):
        self.stopapp()
        self.d.app_start(self.packagename)
        self.outPutMyLog('启动包名为[%s]的应用---------'% self.packagename)
        # self.outPutMyLog('设备信息：', d.device_info)
        self.delaytime(3)

    #关闭app
    def stopapp(self):
        self.d.app_stop(self.packagename)
        self.outPutMyLog('关闭包名为[%s]的应用---------'% self.packagename)

    #延时
    def delaytime(self,dalaytime):
        dalaytime = int(dalaytime)
        time.sleep(dalaytime)
        self.outPutMyLog('等待%d秒...'% dalaytime)

    #点击返回按钮
    def clickback(self):
        self.d.press("back")
        self.outPutMyLog('点击返回按键')
        self.delaytime(3)

    #点击Home按钮
    def clickhome(self):
        self.d.press("home")
        self.outPutMyLog('点击Home按键')
        self.delaytime(3)

    #元素是否存在
    def ele_is_exist(self,findstyle,styleparame):
        try:
            if findstyle == "resourceId":
                ele = self.d(resourceId=styleparame)
                ele.info
                # self.outPutMyLog("ele.info:%s" % ele.info)
                # self.outPutMyLog("找到元素")
            elif findstyle == "text":
                ele = self.d(text=styleparame)
                ele.info
                # self.outPutMyLog("ele.info:%s"% ele.info)
                # self.outPutMyLog("找到元素")
        except Exception as e:
            # self.outPutMyLog("报错：%s"% e)
            return False
        else:
            return True

    #查找元素
    def findelement(self,findstyle,styleparame):
        try:
            if findstyle == "resourceId":
                ele = self.d(resourceId=styleparame)
                eletext = self.geteleinfo_text(ele)
                if eletext == "":
                    self.outPutMyLog("定位到resourceId为[%s]的控件。" % styleparame)
                else:
                    self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
                return ele
            elif findstyle == "text":
                ele = self.d(text=styleparame)
                eletext = self.geteleinfo_text(ele)
                if eletext == "":
                    self.outPutMyLog("没有定位到控件。")
                else:
                    self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
                return ele

        except Exception as e:
            self.outPutMyLog("self.isstartappd的值为：%s"%self.isstartapp)
            self.isstartapp=True
            self.outPutMyLog("self.isstartappd的值为：%s"% self.isstartapp)
            self.getScreenshotError()
            self.outPutErrorMyLog("出错原因：定位控件失败.具体原因：%s"% e)
            self.delaytime(3)
            self.isstartapp=True
            self.outPutMyLog("self.isstartappd的值为：%s"% self.isstartapp)


    #查找到元素并且输入内容
    def findelement_and_input(self,findstyle,styleparame,inputtext):
        ele = self.findelement(findstyle,styleparame)
        self.ele_input(ele, inputtext)

    # 查找到元素并且点击该元素
    def findelement_and_click(self,findstyle,styleparame,outpretoastmessage=None):
        ele = self.findelement(findstyle,styleparame)
        toastmessage = self.ele_click_and_return_toastmessage(ele,outpretoastmessage)
        return toastmessage

    # 查找到元素并且返回enabled属性的状态
    def findelement_and_return_enabledstatus(self,findstyle,styleparame):
        ele = self.findelement(findstyle, styleparame)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    # 查找到元素并且text内容
    def findelement_and_return_text(self,findstyle,styleparame):
        ele = self.findelement(findstyle, styleparame)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    # 查找到元素并且返回selected属性状态
    def findelement_and_return_selectedstatus(self,findstyle,styleparame):
        ele = self.findelement(findstyle, styleparame)
        eleinfo_selected= self.geteleinfo_selected(ele)
        return eleinfo_selected

    #通过ID查找到元素
    def findbyresourceId(self,resourceId):
        d = self.d
        try:
            ele = d(resourceId=resourceId)
            eletext = self.geteleinfo_text(ele)
            if eletext == "":
                self.outPutMyLog("定位到resourceId为[%s]的控件。" % resourceId)
            else:
                self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
            return ele
        except Exception as e:
            self.outPutMyLog("self.isstartappd的值为：%s"% self.isstartapp)
            self.isstartapp=True
            self.outPutMyLog("self.isstartappd的值为：%s"% self.isstartapp)
            self.getScreenshotError()
            self.outPutErrorMyLog("出错原因：定位控件失败.具体原因：%s"% e)
            self.delaytime(3)
            self.isstartapp=True
            self.outPutMyLog("self.isstartappd的值为：%s"% self.isstartapp)

    #通过ID查找到元素并且输入内容
    def findbyresourceId_and_input(self,resourceId,inputtext):
        ele = self.findbyresourceId(resourceId)
        self.ele_input(ele, inputtext)

    # 通过ID查找到元素并且点击该元素
    def findbyresourceId_and_click(self,resourceId,outpretoastmessage=None):
        ele = self.findbyresourceId(resourceId)
        toastmessage = self.ele_click_and_return_toastmessage(ele,outpretoastmessage)
        return toastmessage

    # 通过ID查找到元素并且返回enabled属性的状态
    def findbyresourceId_and_return_enabledstatus(self,resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    # 通过ID查找到元素并且text内容
    def findbyresourceId_and_return_text(self,resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    # 通过ID查找到元素并且返回selected属性状态
    def findbyresourceId_and_return_selectedstatus(self,resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_selected= self.geteleinfo_selected(ele)
        return eleinfo_selected

    #通过text查找到元素
    def findbytext(self,text):
        d = self.d
        try:
            ele = d(text=text)
            eletext = self.geteleinfo_text(ele)
            if eletext == "":
                self.outPutMyLog("没有定位到控件。")
            else:
                self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
            return ele
        except Exception as e:
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)
            self.isstartapp=True
            self.outPutMyLog("self.isstartappd的值为：%s"% self.isstartapp)
            self.getScreenshotError()
            self.outPutErrorMyLog("出错原因：定位控件失败.具体原因：%s"% e)
            self.delaytime(3)


    #通过text查找到元素并且输入内容
    def findbytext_and_input(self,text, inputtext):
        ele = self.findbytext(text)
        self.ele_input(ele,inputtext)

    #通过text查找到元素并且点击内容
    def findbytext_and_click(self,text,outpretoastmessage=None):
        ele = self.findbytext(text)
        toastmessage = self.ele_click_and_return_toastmessage(ele,outpretoastmessage)
        return toastmessage

    #通过text查找到元素并且返回enabled状态
    def findbytext_and_return_enabledstatus(self,text):
        ele = self.findbytext(text)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    #通过text查找到元素并且返回enabled状态
    def findbytext_and_return_text(self,text):
        ele = self.findbytext(text)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    #通过text查找到元素并且返回selected状态
    def findbytext_and_return_selectedstatus(self,text):
        ele = self.findbytext(text)
        eleinfo_selected= self.geteleinfo_selected(ele)
        return eleinfo_selected

    #元素中输入内容
    def ele_input(self,ele,inputtext):
        ele.clear_text()
        ele.send_keys(inputtext)
        self.outPutMyLog("输入:%s。" % inputtext)
        self.delaytime(1)

    #点击元素并返回toast提示信息
    def ele_click_and_return_toastmessage(self,ele,outpretoastmessage=None):
        ele.click()
        self.outPutMyLog("点击该控件。")
        if outpretoastmessage==None:
            self.delaytime(3)
            return None
        else:
            toastmessage = self.getToast()
            self.outPutMyLog("pretoastmessage:",outpretoastmessage)
            return toastmessage

    #得到元素enabled属性值
    def geteleinfo_enabled(self,ele):
        value = 'enabled'
        eleinfo_enabled = self.geteleinfo_value(ele,value)
        self.outPutMyLog('该控件的enabled属性的值为：%s'%eleinfo_enabled)
        return eleinfo_enabled

    #得到元素text属性值
    def geteleinfo_text(self,ele):
        value = 'text'
        eleinfo_text = self.geteleinfo_value(ele,value)
        if eleinfo_text !='':
            self.outPutMyLog('该控件的text属性的值为：%s'% eleinfo_text)
        return eleinfo_text

    #得到元素selected属性值
    def geteleinfo_selected(self,ele):
        value = 'selected'
        eleinfo_selected = self.geteleinfo_value(ele,value)
        if eleinfo_selected !='':
            self.outPutMyLog('该控件的selected属性的值为：%s'% eleinfo_selected)
        return eleinfo_selected

    #得到元素属性值
    def geteleinfo_value(self,ele,value):
        eleinfo = ele.info
        # self.outPutMyLog('eleinfo:',eleinfo)
        eleinfo_value = eleinfo[value]
        return eleinfo_value

    #得到toast提示信息
    def getToast(self):
        toastmessage = self.d.toast.get_message(5.0, default="")
        self.outPutMyLog("toastmessage:",toastmessage)
        return toastmessage

    #得到设备信息
    def getdeviceinfo(self):
        deviceinfo = self.d.device_info
        self.outPutMyLog("deviceinfo:%s"%deviceinfo)
        self.outPutMyLog("deviceinfo类型:%s"% type(deviceinfo))
        return deviceinfo

    #建立crash监听
    def createwatcher(self):
        d = self.d
        d.watcher('crash').when(text='很抱歉，“QRindo MCH”已停止运行。').click(text="确定")
        d.watcher("crash").triggered
        self.outPutMyLog('d.watcher:',d.watcher)


    #获取时间串
    def getTimeStr(self):
        tStr = self.timeStr.getTimeStr()
        return tStr

    def getTimeStrNY(self):
        tStrNY = self.timeStr.getTimeStrNY()
        return tStrNY

    #出错时，获取页面截图
    def getScreenshotError(self):
        d = self.d
        self.outPutMyLog("调用截取图片函数")
        currentny = self.getTimeStrNY()   #获取当前时间的年月
        tStr = self.getTimeStr()
        # path = "../screenshots/screenpicture_%s.png"% tStr
        firedir = r'%s/media/report/%s/screenshots/' % (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),currentny)
        self.createdir(firedir)
        path = '%s/screenpicture_%s.png' % (firedir,tStr)
        pathaboutmysql = r'media\report\%s\screenshots\screenpicture_%s.png' % (currentny, tStr)
        # path = '%s/screenshots/screenpicture_%s.png'%(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),tStr)
        d.screenshot(path)
        self.outPutMyLog("*****")
        # self.outPutMyLog(path)
        self.outPutMyLog(pathaboutmysql)
        self.outPutMyLog("*****")
        return path

    #正常，获取页面截图
    def getScreenshotNormal(self):
        d = self.d
        self.outPutMyLog("调用截取图片函数")
        tStr = self.getTimeStr()
        # path = "../screenshots/screenpicture_%s.png"% tStr
        path = '%s/screenshots/screenpicture_%s.png' % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), tStr)
        d.screenshot(path)
        self.outPutMyLog("*****")
        self.outPutMyLog(path)
        self.outPutMyLog("*****")
        return path

    def createdir(self,filedir):
        filelist = filedir.split("/")
        # print(filelist)
        long = len(filelist)
        # print(long)
        zuhefiledir = filelist[0]
        for i in range(1,long):
            zuhefiledir = zuhefiledir+"/"+filelist[i]
            if os.path.exists(zuhefiledir):
                self.outPutMyLog("已经存在目录：%s" % zuhefiledir)
            else:
                os.mkdir(zuhefiledir)
                self.outPutMyLog("已经创建目录：%s" % zuhefiledir)



if __name__ == "__main__":
    outdevice = "192.168.1.100:5555"
    apppacakagename = "com.tencent.tmgp.sgame"

    bf = BaseFrame(outdevice=outdevice,apppacakagename=apppacakagename)
    # bf.findbytext_and_click(outpretoastmessage='',text="Show QR")
    # dv = bf.getdeviceinfo()
    # print(dv["model"])
    # print(dv["version"])
    # print(dv["display"]["width"])
    # print(dv["display"]["height"])
    bf.startapp()











