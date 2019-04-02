# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/26 14:59'
import time   #导入时间
import os
import traceback
import json

from selenium import webdriver   #导入驱动
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from PIL import Image   #导入Image
from PIL import ImageEnhance  #导入ImageEnhance
import pytesseract   #导入pytesseract
from selenium.webdriver.support.select import Select   #导入Select

from selenium.webdriver.common.action_chains import ActionChains   #导入ActionChains


from TestCaseFunction.util.gettimestr import GetTimeStr   #导入获取时间串函数



class  ActiveWeb:
    def __init__(self):
        # self.driver = self.getChromeDriver()
        # self.driver = self.getIeDriver()
        self.driver = self.getFirefoxDriver()
        self.timeStr = GetTimeStr()   #实例化

    #使用火狐浏览器
    def getFirefoxDriver(self):
        # binary = FirefoxBinary(r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        # firefoxdriver = webdriver.Firefox(firefox_binary=binary)
        firefoxdriver = webdriver.Firefox()  # 需要把驱动所在路径配置到系统环境变量里
        firefoxdriver.maximize_window()   #窗口最大化
        return  firefoxdriver

    #使用谷歌浏览器
    def getChromeDriver(self):
        chromedriver = webdriver.Chrome()  # 需要把驱动所在路径配置到系统环境变量里
        return  chromedriver

    #使用IE浏览器
    def getIeDriver(self):
        iedriver = webdriver.Ie()  # 需要把驱动所在路径配置到系统环境变量里
        return  iedriver

    #使用Edge浏览器
    def getEdgeDriver(self):
        edgedriver = webdriver.Edge()  # 需要把驱动所在路径配置到系统环境变量里
        return  edgedriver

    #使用Opera浏览器
    def getOperaDriver(self):
        operadriver = webdriver.Opera  # 需要把驱动所在路径配置到系统环境变量里
        return  operadriver

    #打开网址
    def getUrl(self,url):
        self.driver.get(url)
        print("进入网址：%s"% url)

    #通过xpath查找元素
    def findElementByXpath(self,path):
        try:
            ele = self.driver.find_element_by_xpath(path)
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,"background:green;border:2px solid red")   #高亮显示操作的元素
            #使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜分别设置为绿色和红色
        except Exception as e:
            print(e)
            self.getScreenshotNormal()
            self.delayTime(5)
        finally:
            try:
                ele = self.driver.find_element_by_xpath(path)
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
                self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,"background:green;border:2px solid red")  # 高亮显示操作的元素
                # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜分别设置为绿色和红色
                # print("最终找到元素")
            except Exception as e:
                self.printredword()
                self.getScreenshot()
                print("停顿5秒后再次查找依然未找到元素，关闭驱动.问题描述：",e)
                self.printnormalword()
                self.closeBrowse()
        return ele

    #获取控件截图
    def getEleImage(self,num,path):
        ele = self.findElementByXpath(path)   #获取元素控件
        pageScreenshotpath = self.getScreenshotNormal()  # 获取整个页面截图
        # location = ele.location   #获取验证码x,y轴坐标   #截取了BUSINESS
        location = ele.location_once_scrolled_into_view  # 获取元素x,y轴坐标   #消除self.driver.execute_script("arguments[0].scrollIntoView();", ele) 对截图的影响 截取了login imgae
        size = ele.size   #获取元素的长宽
        coderange = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        pageScreenshot = Image.open(pageScreenshotpath)   #打开截图
        imageScreen = pageScreenshot.crop(coderange)   #使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
        tStr = self.getTimeStr()
        eleimage = "../imagefile/ele/%s_%s_ele.png" % (num,tStr)
        imageScreen.save(eleimage)   #保存控件截图
        print('找到的ele的截图：', eleimage)
        return ele


    #通过xpath查找元素，然后返回元素的text内容
    def findElementByXpathAndReturnText(self,num,path):
        ele = self.getEleImage(num,path)
        eletext = ele.text
        return eletext




    #通过xpath查找元素，然后返回元素的标签名(例如input)
    def findElementByXpathAndReturnTagName(self,path):
        ele = self.findElementByXpath(path)
        eletext = ele.tag_name
        return eletext

    #通过xpath查找元素，然后返回元素的默认显示文字
    def findElementByXpathAndReturnValue(self,path,valuename):
        ele = self.findElementByXpath(path)
        eletext = ele.get_attribute(valuename)
        return eletext

    #通过xpath查找元素，然后输入内容
    def findElementByXpathAndInput(self,path,inputcontent):
        ele = self.findElementByXpath(path)
        ele.clear()   #清除输入框内容
        ele.send_keys(inputcontent)   #输入内容

    #通过xpath查找元素，然后输入内容
    def findElementByXpathAndInputNum(self,num,path,inputcontent):
        ele = self.getEleImage(num, path)
        ele.clear()   #清除输入框内容
        ele.send_keys(inputcontent)   #输入内容

    #通过xpath查找元素，然后点击
    def findElementByXpathAndClick(self,path):
        ele = self.findElementByXpath(path)
        ele.click()   #点击
        print("点击元素的Xpath路径为：%s" % path)
        self.delayTime(3)
        return ele

    #通过xpath查找元素，然后点击
    def findElementByXpathAndScriptClick(self,path):
        ele = self.findElementByXpath(path)
        self.driver.execute_script("arguments[0].click();", ele)
        return ele

    #通过xpath查找到要输入文件的input元素，然后上传文件
    def findElementByXpathAndAndFile(self,path,filepath):
        ele = self.findElementByXpath(path)
        try:
            ele.send_keys(filepath)
            self.delayTime(1)
        except Exception as e:
            self.printredword()
            print("上传文件失败，关闭驱动.问题描述：",e)
            self.printnormalword()
            self.closeBrowse()


    #通过xpath查找到select元素,选择要选择的项
    def findElementByXpathAndReturnOptions(self,path,optiontext):
        ele = Select(self.findElementByXpath(path))
        try:
            selectoption = ele.select_by_visible_text(optiontext)
            self.delayTime(2)
        except Exception as e:
            self.printredword()
            print("填写内容与选项内容对不上，关闭驱动.问题描述：",e)
            self.printnormalword()
            self.closeBrowse()

    #通过xpath查找到select并打印其所有的options
    def findElementByXpathAndReturnAllOptions(self,path):
        ele = Select(self.findElementByXpath(path))
        optionlist = []
        try:
            all_options = ele.options
            # print('所有选项内容如下：',all_options)
            for option in all_options:
                optionlist.append(option.text)
                # print('选项内容为：',option.text)
            print('获取的选项所有内容：',optionlist)
            return optionlist
        except Exception as e:
            self.printredword()
            print("获取选项内容出错，关闭驱动.问题描述：",e)
            self.printnormalword()
            self.closeBrowse()

    #通过xpath查找到tbody并打印表格里所有内容
    def findElementByXpathAndReturnTable(self,path):
        ele = self.findElementByXpath(path)
        # print('tagname:',ele.tag_name)
        tabledic = {}
        try:
            trlist = ele.find_elements_by_tag_name('tr')
            # print(len(trlist))
            for i in range(0,len(trlist)):
                # print('第%s行内容如下:\n'% str(i+1))
                #遍历行对象，并获取每一行中所有列对象
                tdlist = trlist[i].find_elements_by_tag_name('td')
                collist = []
                for j in range(0,len(tdlist)):
                    #遍历表格中的列，并打印单元格内容
                    collist.append(tdlist[j].text)
                    # print('第%s列内容如下：'% str(j+1),tdlist[j].text)
                    tabledic[i+1] = collist
            print('获取的表格内容：',tabledic)
            return tabledic
            # print('列表内容为：',option.text)
        except Exception as e:
            self.printredword()
            print("获取表格内容出错，关闭驱动.问题描述：",e)
            self.printnormalword()
            self.closeBrowse()

    #通过xpath查找到tbody并打印表格里所有内容
    def findElementByXpathAndReturnTableNum(self,num,path):
        ele = self.getEleImage(num,path)
        # print('tagname:',ele.tag_name)
        tabledic = {}
        try:
            trlist = ele.find_elements_by_tag_name('tr')
            # print(len(trlist))
            for i in range(0,len(trlist)):
                # print('第%s行内容如下:\n'% str(i+1))
                #遍历行对象，并获取每一行中所有列对象
                tdlist = trlist[i].find_elements_by_tag_name('td')
                collist = []
                for j in range(0,len(tdlist)):
                    #遍历表格中的列，并打印单元格内容
                    collist.append(tdlist[j].text)
                    # print('第%s列内容如下：'% str(j+1),tdlist[j].text)
                    tabledic[i+1] = collist
            print('获取的表格内容：',tabledic)
            return tabledic
            # print('列表内容为：',option.text)
        except Exception as e:
            self.printredword()
            print("获取表格内容出错，关闭驱动.问题描述：",e)
            self.printnormalword()
            self.closeBrowse()

    def checktable(self,path,inputtext,colnum):
        tabledic = self.findElementByXpathAndReturnTable(path)
        for value in tabledic.values():
            if inputtext.lower() in value[colnum].lower():
                print('input输入内容变小写：',inputtext.lower())
                print('搜索到的表格内容变小写：',value[colnum].lower())
            else:
                print("搜索到的内容不匹配！！！")

    #获取页面截图
    def getScreenshot(self):
        driver = self.driver
        self.printredword()
        print("调用截取图片函数")
        tStr = self.getTimeStr()
        path = "../imagefile/%s.png"% tStr
        path = '%s/screenshots/screenpicture_%s.png' % (
        str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), tStr)
        self.printnormalword()
        driver.get_screenshot_as_file(path)
        print("*****")
        print(path)
        print("*****")
        return path

    #获取页面截图
    def getScreenshotNormal(self):
        driver = self.driver
        print("调用截取图片函数")
        tStr = self.getTimeStr()
        path = "../imagefile/%s.png"% tStr
        driver.get_screenshot_as_file(path)
        return path

    #获取code码截图
    def getCodeImage(self,path):
        pageScreenshotpath = self.getScreenshotNormal()  # 获取整个页面截图
        image = self.findElementByXpath(path)   #获取图片验证码控件
        # location = image.location   #获取验证码x,y轴坐标
        location = image.location_once_scrolled_into_view  # 获取验证码x,y轴坐标   #消除self.driver.execute_script("arguments[0].scrollIntoView();", ele) 对截图的影响
        size = image.size   #获取验证码的长宽
        coderange = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        pageScreenshot = Image.open(pageScreenshotpath)   #打开截图
        imageScreen = pageScreenshot.crop(coderange)   #使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
        tStr = self.getTimeStr()
        path = "../imagefile/%s_code.png"%tStr
        imageScreen.save(path)   #保存验证码图片
        return tStr

    #获取验证码文字信息
    def getcodetext(self,path):
        imagecodestr = self.getCodeImage(path)
        imagecode = Image.open("../imagefile/%s_code.png" % imagecodestr)  # 打开验证码图片
        pixtongji = []
        for x in range(imagecode.size[1]):
            for y in range(imagecode.size[0]):
                # 遍历图片的xy坐标像素点颜色
                pix = imagecode.getpixel((y, x))
                pixtongji.append(pix)
        nonepixtongjidic = {}
        for item in pixtongji:
            if item in nonepixtongjidic.keys():
                nonepixtongjidic[item] += 1
            else:
                nonepixtongjidic[item] = 1

        print("nonepixtongjidic:",nonepixtongjidic)
        nonepixtongjilist = sorted(nonepixtongjidic.values(),reverse=True)   #按照键值对的值对字典进行倒序排序
        numvalue = []
        numvalue.append(nonepixtongjilist[1])   #获取第二个值
        getkey = self.getDictKey(nonepixtongjidic,numvalue)
        img_new = Image.new('P', imagecode.size, 255)
        for x in range(imagecode.size[1]):
            for y in range(imagecode.size[0]):
                # 遍历图片的xy坐标像素点颜色
                pix = imagecode.getpixel((y, x))
                # print(pix)
                # 自己调色，r（pix[0]）=0，g（pix[1]）=0，b（pix[2]）>0为蓝色
                for i in range(len(getkey)):
                    if (pix[0] == getkey[i][0] and pix[1] == getkey[i][1] and pix[2] == getkey[i][2]):
                        # 把遍历的结果放到新图片上，0为透明度，不透明
                        img_new.putpixel((y, x), 0)
        newpath = "../imagefile/%s_codegary.png" % imagecodestr
        img_new.save(newpath, format='png')

        imagecode = Image.open(newpath)   #打开验证码图片
        imgry = imagecode.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(imgry)   #对比度增强
        imagecodegary = sharpness.enhance(2.0)#2.0为图像的饱和度
        imagecodegary.save(newpath)   #保存灰度值验证码
        endcode = Image.open(newpath)    #打开灰度值验证码
        codetext = pytesseract.image_to_string(endcode).strip()   #获取验证码文本文件
        return codetext


    #获取字典对应值的键
    def getDictKey(self,dict,prevalue):
        getkey = []
        for key,value in dict.items():
            for i in range(len(prevalue)):
                if value == prevalue[i]:
                    getkey.append(key)
        return getkey

    #获取时间串
    def getTimeStr(self):
        tStr = self.timeStr.getTimeStr()
        return tStr


    #获取cookies
    def getCookies(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print("获取的cookie的值为：%s" % cookie)
        return cookies

    #写入cookies
    def writerCookies(self,cookies,url,url2):
        print("\n开始写入cookie-----------------\n")
        self.getUrl(url)
        long = len(cookies)
        for i in range(long):
            cookie = {'name': cookies[i]['name'], 'value': cookies[i]['value']}
            self.driver.add_cookie(cookie)   #selenium添加cookies时，得先登录网址才能添加cookies的
            print("写入cookie的值为：%s" % cookie)
        self.driver.refresh()  #
        print("刷新当前页面---------")
        self.getUrl(url2)
        print("url2为：%s."%url2)
        self.driver.refresh()   #刷新当前页面
        print("刷新当前页面---------")
        self.delayTime(5)   #等待10秒
        self.getCookies()

    #打印红色文字
    def printredword(self):
        print('\033[1;31;0m')   #<!--1-高亮显示 31-前景色红色  47-背景色白色-->

    #打印默认文字
    def printnormalword(self):
        print('\033[0m')  # <!--采用终端默认设置，即取消颜色设置-->

    #打印绿色文字
    def printgreenword(self):
        print('\033[1;32;0m')  # <!--1-高亮显示 32-前景色绿色  40-背景色黑色-->

    #延迟3秒
    def delayTime(self,dalaytime):
        time.sleep(int(dalaytime))   #延迟，
        print("等待%s秒---"% dalaytime)



    #关闭浏览器
    def closeBrowse(self):
        self.driver.quit()


if __name__ == "__main__":
    activeweb = ActiveWeb() #实例化
    url = "https://bjw.halodigit.com:9090/nereus/manager/index"
    activeweb.getUrl(url)
    # activeweb.delaytime(30)
    # activeweb.findElementByXpathAndInput("/html/body/div[1]/div[2]/form/div/div[1]/input","xiangkaizheng@iapppay.com")   #输入账号名
    # activeweb.findElementByXpathAndInput("/html/body/div[1]/div[2]/form/div/div[2]/input","123456")   #输入密码
    # activeweb.findElementByXpathAndClick("/html/body/div[1]/div[2]/form/div/a[1]/span")   #点击登录












