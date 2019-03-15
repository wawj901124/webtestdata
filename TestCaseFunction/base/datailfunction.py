# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/26 18:27'

from base.activebase import ActiveWeb

class WebFunction:
    def __init__(self):
        self.activeweb = ActiveWeb()

    def assertresult(self,testresult,preresult):
        message = [1,2]
        if testresult == preresult:
            self.activeweb.printgreenword()
            passmessage = "测试通过-描述【预期结果为：%s,实际结果为：%s,两者一致。】" % (preresult,testresult)
            print(passmessage)
            self.activeweb.printnormalword()
            message[0] = 'pass'
            message[1] = passmessage
        else:
            self.activeweb.printredword()
            failmessage = "测试失败-失败描述【预期结果为：%s,而实际结果为：%s,两者不一致。】" % (preresult,testresult)
            print(failmessage)
            self.activeweb.printnormalword()
            message[0] = 'fail'
            message[1] = failmessage
        return message



    def assertText(self,num,testxpath,preresult):
        testresult = self.activeweb.findElementByXpathAndReturnText(num,testxpath)
        assertresult = self.assertresult(testresult,preresult)
        return assertresult

    def assertSelectSearch(self,num,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext):
        message = [1, 2]
        flag = False
        self.activeweb.findElementByXpathAndReturnOptions(selectxpath,str(selectoptiontext))
        self.activeweb.findElementByXpathAndInput(selectinputxpath,str(selectinputtext))
        self.activeweb.findElementByXpathAndClick(searchbuttonxpath)
        self.activeweb.delayTime(5)
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num,searchtableresultxpath)
        for value in tabledic.values():
            if str(checktext).lower() in value[int(colnum)].lower():
                flag = True
        if flag:
            self.activeweb.printgreenword()
            passmessage = "测试通过-描述【预期搜索结果中包含：%s,实际搜索结果为：%s,符合预期。】" % (str(checktext),tabledic)
            print(passmessage)
            self.activeweb.printnormalword()
            message[0] = 'pass'
            message[1] = passmessage
        else:
            self.activeweb.printredword()
            failmessage = "测试失败-失败描述【预期搜索结果中包含：%s,实际搜索结果为：%s,不符合预期。】" % (str(checktext),tabledic)
            print(failmessage)
            self.activeweb.printnormalword()
            message[0] = 'fail'
            message[1] = failmessage
        return message




    def assertInputValue(self,testxpath,testvaluename,preresult):
        testresult = self.activeweb.findElementByXpathAndReturnValue(testxpath,testvaluename)
        self.assertresult(testresult,preresult)





