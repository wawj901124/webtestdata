import unittest

from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_AGENT_LOGIN_ACCOUNT,TEST_AGENT_LOGIN_PASSWORD   #导入测试环境参数
from webtestdata.settings import ONLINE_AGENT_LOGIN_ACCOUNT,ONLINE_AGENT_LOGIN_PASSWORD  #导入现网环境参数


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson
from TestCaseFunction.util.gettimestr import GetTimeStr

from TestCaseFunction.autotest.config.page.agent180.loginPage import LoginPage
from TestCaseFunction.autotest.config.page.agent180.addIndividuMerchantPage import AddIndividuMerchantPage
from TestCaseFunction.autotest.config.page.agent180.addMerchantSuccessPage import AddMerchantSuccessPage
from TestCaseFunction.autotest.config.page.agent180.addMerchantDonePage import AddMerchantDonePage
from TestCaseFunction.autotest.config.page.agent180.merchantListPage import MerchantListPage
from TestCaseFunction.autotest.config.page.agent180.IndividuDetailsPage import IndividuDetailsPage



class TestAddMerchantClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        # from base.getcookie import GetCookie
        # outjsonfile = "../../../cookiejson/cookiemanager.json"
        # outloginurl = LoginPage().pageurl
        # outloginaccountxpath = LoginPage().account
        # outloginaccounttext = "81122336666"
        # outloginppasswordxpath = LoginPage().password
        # outloginpasswordtext = "abc123456"
        # outloginbuttonxpath = LoginPage().loginbutton
        #
        # getcookie = GetCookie(outjsonfile=outjsonfile, outloginurl=outloginurl,
        #                       outloginaccountxpath=outloginaccountxpath,
        #                       outloginaccounttext=outloginaccounttext, outloginppasswordxpath=outloginppasswordxpath,
        #                       outloginpasswordtext=outloginpasswordtext,
        #                       outloginbuttonxpath=outloginbuttonxpath)  # 实例化
        # getcookie.writerCookieToJson()

        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        # self.jsonfile = '../../../cookiejson/cookieagent.json'
        # self.operationjson = OperationJson(file_path=self.jsonfile)   #实例化
        # self.cookie = self.operationjson.get_all_data()
        # print("self.cookie:%s" % self.cookie)
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = LoginPage().pageurl
        self.activeweb.getUrl(self.loginurl)  # 打开网址
        if ISONLINE:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,ONLINE_AGENT_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,ONLINE_AGENT_LOGIN_PASSWORD)
        else:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,TEST_AGENT_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,TEST_AGENT_LOGIN_PASSWORD)

        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = AddIndividuMerchantPage()
        self.testpageurl =self.testpage.pageurl   #测试页面url
        self.testpagemerchantinfo = self.testpage.merchantinfo   #Merchant info中 元素
        self.testpagebrandnameinput = self.testpage.brandnameinput
        self.testpageemailinput = self.testpage.emailinput
        self.testpagecontactnumberinput = self.testpage.contactnumberinput
        self.testpagemerchanttypeselect = self.testpage.merchanttypeselect
        self.testpagecategoryselect = self.testpage.categoryselect
        self.testpagecriteriaselect = self.testpage.criteriaselect
        self.testpagesiupinput = self.testpage.siupinput
        self.testpageprovinceselect = self.testpage.provinceselect
        self.testpagecityselect = self.testpage.cityselect
        self.testpagedistrictinput = self.testpage.districtinput
        self.testpagevillageinput = self.testpage.villageinput
        self.testpagepostcodeinput = self.testpage.postcodeinput
        self.testpageaddressinput = self.testpage.addressinput
        self.testpagephotosiupimage = self.testpage.photosiupimage
        self.testpagephotonpwpcompanyimage = self.testpage.photonpwpcompanyimage
        self.testpagephototdpimage = self.testpage.phototdpimage
        self.testpageownerpersoninchargeinfo = self.testpage.ownerpersoninchangeinfo #Owner / Person in Charge info中 元素
        self.testpagenameinput = self.testpage.nameinput
        self.testpagenpwpinput = self.testpage.npwpinput
        self.testpagetypeidselect = self.testpage.typeidselect
        self.testpageidentitynumberinput = self.testpage.identitynumberinput
        self.testpageaddress2input = self.testpage.address2input
        self.testpagenationalityselect = self.testpage.nationalityselect
        self.testpagephoneinput = self.testpage.phoneinput
        self.testpageemail2input = self.testpage.email2input
        self.testpagephotofullfacebustimage = self.testpage.photofullfacebustimage
        self.testpageprofilephotos = self.testpage.profilephotos    #Profile Photos中 元素
        self.testpagelocationphotoimage = self.testpage.locationphotoimage
        self.testpagephotoofthecashiersdeskimage = self.testpage.photoofthecashiersdeskimage
        self.testpageotherphotoimage = self.testpage.otherphotoimage
        self.testpagebankaccount = self.testpage.bankaccount  #Bank account中 元素
        self.testpagebankselect = self.testpage.bankselect
        self.testpageaccountnameinput = self.testpage.accountnameinput
        self.testpageaccountnumberinput = self.testpage.accountnumberinput
        self.testpageqrindoaccount = self.testpage.qrindoaccount  #QRindo account中 元素
        self.testpageqrindoaccountinput = self.testpage.qrindoaccountinput
        self.testpagecheckbutton = self.testpage.checkbutton
        self.testpagesubmitbutton = self.testpage.submitbutton
        self.testpageresetbutton = self.testpage.resetbutton
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    def writexunicookie(self):
        addcookie = {'name': '.nereus.manager.settle.banks', 'value': 'QCK9GvKG8OEOh6lRUyyLlmKnHl8i3w'}
        self.activeweb.driver.add_cookie(addcookie)
        self.activeweb.driver.refresh()
        self.activeweb.delayTime(5)
        self.activeweb.outPutMyLog("写入虚拟银行cookie完成")




    #定义搜索查找函数
    def defineaddmerchantindividu(self, num, isfictitious=False,brandnameinputtext=None, emailinputtext=None, contactnumberinputtext=None,  #添加个人商户
                          merchanttypeselectoptionxpath=None, categoryselectoptionxpath=None, criteriaselectoptionxpath=None,
                          siupinputtext=None, provinceselectoptionxpath=None, cityselectoptionxpath=None,
                          districtinputtext=None, villageinputtext=None, postcodeinputtext=None,addressinputtext=None,
                          photosiupimagefilepath=None, photonpwpcompanyimagefilepath=None, phototdpimagefilepath=None,
                          nameinputtext=None, npwpinputtext=None, typeidselectoptionxpath=None,
                          identitynumberinputtext=None, address2inputtext=None, nationalityselectoptionxpath=None,
                          phoneinputtext=None, email2inputtext=None, photofullfacebustimagefilepath=None,
                          locationphotoimagefilepath=None, photoofthecashiersdeskimagefilepath=None, otherphotoimagefilepath=None,
                          bankselectoptionxpath=None, accountnameinputtext=None, accountnumberinputtext=None,
                          qrindoaccountinputtext=None):
        # self.activeweb.writerCookies(self.cookie, LoginPage().pageurl,MerchantListPage().pageurl)
        if isfictitious:
            self.writexunicookie()
        # self.activeweb.delayTime(5000)
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #添加个人商户
        #添加Basic info信息
        self.activeweb.findElementByXpathAndInputNum(num, self.testpageemailinput, emailinputtext)  # 输入Email,必填字段
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagebrandnameinput, brandnameinputtext)   #输入Brand name，必填字段

        #添加Merchant info信息
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpagecontactnumberinput, contactnumberinputtext)   #输入Contact number
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagemerchanttypeselect,merchanttypeselectoptionxpath)  # 选择Merchant type，必填字段
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecategoryselect, categoryselectoptionxpath)   # 选择Category，必填字段
        if criteriaselectoptionxpath != None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecriteriaselect,criteriaselectoptionxpath)  # 选择Criteria，选填字段
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpagesiupinput, siupinputtext)  # 输入SIUP
        if provinceselectoptionxpath !=None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpageprovinceselect,provinceselectoptionxpath)  # 选择Province，选填字段
        if cityselectoptionxpath !=None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecityselect,cityselectoptionxpath)  # 选择City，选填字段
        if districtinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagedistrictinput, districtinputtext)  # 输入District，选填字段
        if villageinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagevillageinput,villageinputtext)  # 输入Village，选填字段
        if postcodeinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagepostcodeinput, postcodeinputtext)  # 输入Postcode，选填字段
        if addressinputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpageaddressinput, addressinputtext)  # 输入Address，选填字段
        if photonpwpcompanyimagefilepath !=None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotonpwpcompanyimage,photonpwpcompanyimagefilepath)  # 添加Photo NPWP Company图片，选填字段
        if phototdpimagefilepath != None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephototdpimage,phototdpimagefilepath)  # 添加Photo TDP图片，选填字段

        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpagemerchantinfo)  #点击Merchant info
        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageownerpersoninchargeinfo)  # 点击Owner / Person in Charge info

        #添加Owner / Person in Charge info信息
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagenameinput, nameinputtext)  # 输入Name，必填字段
        if npwpinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagenpwpinput, npwpinputtext)  # 输入NPWP，选填字段
        if typeidselectoptionxpath != None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagetypeidselect,typeidselectoptionxpath)  # 选择ID Type，选填字段
        if identitynumberinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpageidentitynumberinput, identitynumberinputtext)  # 输入Identity number，选填字段
        if address2inputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpageaddress2input, address2inputtext)  # 输入Address，选填字段
        if nationalityselectoptionxpath != None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagenationalityselect,nationalityselectoptionxpath)  # 选择Nationality，选填字段
        if phoneinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagephoneinput, phoneinputtext)  # 输入Phone，选填字段
        if email2inputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpageemail2input, email2inputtext)  # 输入Email，选填字段
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotofullfacebustimage,photofullfacebustimagefilepath)  # 添加Photo Full-faceBust图片，必填字段

        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageownerpersoninchargeinfo)  # 点击Owner / Person in Charge info
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpageprofilephotos)  # 点击Profile Photos

        #添加Profile Photos信息
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagelocationphotoimage,locationphotoimagefilepath)  # 添加Location Photo图片，必填字段
        if photoofthecashiersdeskimagefilepath != None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotoofthecashiersdeskimage,photoofthecashiersdeskimagefilepath)  # 添加Photo of the cashiers desk图片，选填字段
        if otherphotoimagefilepath != None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpageotherphotoimage,otherphotoimagefilepath)  # 添加Other Photo图片，选填字段

        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpageprofilephotos)  # 点击Profile Photos
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpagebankaccount)  # 点击Bank account

        #添加Bank account信息
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagebankselect,bankselectoptionxpath)  # 选择Bank，必填字段
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageaccountnameinput, accountnameinputtext)  # 输入Account name，必填字段
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageaccountnumberinput, accountnumberinputtext)  # 输入Account number，必填字段

        #点击Submit按钮
        self.activeweb.findElementByXpathAndClickNum(num,self.testpagesubmitbutton)  # 点击submit按钮

        # self.activeweb.findElementByXpathAndClickNum(num,self.testpageresetbutton)  # 点击reset按钮
        #断言是否有“Success”
        # self.defineasserttextnum(num,AddMerchantSuccessPage().successindividu,AddMerchantSuccessPage().successtext)
        # self.activeweb.findElementByXpathAndClickNum(num,AddMerchantSuccessPage().okbuttonindividu)

        #断言是否有“Done”
        self.defineasserttextnum(num, AddMerchantDonePage().done, AddMerchantDonePage().donetext)
        # 断言是否有“Waiting for approval”
        self.defineasserttextnum(num, AddMerchantDonePage().waitingforapproval, AddMerchantDonePage().waitingforapprovaltext)
        # 断言是否有brandnameinputtext（添加的商户名）
        self.defineasserttextnum(num, AddMerchantDonePage().merchantnamevalue, brandnameinputtext)
        #点击Done页面的Merchant list按钮
        self.activeweb.findElementByXpathAndClickNum(num,AddMerchantDonePage().merchantlistbutton)

        #断言商户列表中是否有新增加的商户名
        self.defineisintable(num,MerchantListPage().searchtableresult,brandnameinputtext,1)
        # self.activeweb.delayTime(1000)
        #点击商户列表新建商户的Detail进入商户详情页；
        self.activeweb.findElementByXpathAndClickNum(num, MerchantListPage().operation_waitingforreview_details)

        #断言详情页中的内容
        #详情页存在Basic info
        self.defineassertdetailstextnum(num,IndividuDetailsPage().basicinfo,IndividuDetailsPage().basicinfotext)
        #断言存在Merchant ID
        self.defineassertdetailstextnum(num,IndividuDetailsPage().merchantid,IndividuDetailsPage().merchantidtext)
        merchantid = self.activeweb.findElementByXpathAndReturnText(num, IndividuDetailsPage().merchantidvalue)   #获取merchantid
        self.activeweb.outPutMyLog("新建商户id：%s" % merchantid)
        # 保存merchantid
        filename = "merchantid.txt"
        GetTimeStr().writeText(filename, merchantid)
        #断言存在Login account
        self.defineassertdetailstextnum(num, IndividuDetailsPage().loginaccount, IndividuDetailsPage().loginaccounttext)
        self.defineassertdetailstextnum(num, IndividuDetailsPage().loginaccountvalue, emailinputtext)
        #断言存在Brand name
        self.defineassertdetailstextnum(num, IndividuDetailsPage().brandname, IndividuDetailsPage().brandnametext)
        self.defineassertdetailstextnum(num, IndividuDetailsPage().brandnamevalue,brandnameinputtext)
        #断言存在agent
        self.defineassertdetailstextnum(num,IndividuDetailsPage().agent,IndividuDetailsPage().agentvalue)

        # 详情页存在Merchant info
        self.defineassertdetailstextnum(num, IndividuDetailsPage().merchantinfo, IndividuDetailsPage().merchantinfotext)
        #断言存在Merchant type
        self.defineassertdetailstextnum(num, IndividuDetailsPage().merchanttype, IndividuDetailsPage().merchanttypetext)
        self.defineassertdetailstextnum(num, IndividuDetailsPage().merchanttypevalue,IndividuDetailsPage().merchanttypevaluetext)
        #断言存在Category
        self.defineassertdetailstextnum(num, IndividuDetailsPage().category, IndividuDetailsPage().categorytext)
        self.defineassertdetailstextnum(num, IndividuDetailsPage().categoryvalue,IndividuDetailsPage().categoryvaluetext)
        #断言存在Criteria
        self.defineassertdetailstextnum(num, IndividuDetailsPage().criteria, IndividuDetailsPage().criteriatext)
        if criteriaselectoptionxpath != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().criteriavalue,IndividuDetailsPage().criteriavaluetext)
        #断言存在Province
        self.defineassertdetailstextnum(num, IndividuDetailsPage().province, IndividuDetailsPage().provincetext)
        if provinceselectoptionxpath != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().provincevalue,IndividuDetailsPage().provincevaluetext)
        #断言存在City
        self.defineassertdetailstextnum(num, IndividuDetailsPage().city, IndividuDetailsPage().citytext)
        if cityselectoptionxpath !=None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().cityvalue,IndividuDetailsPage().cityvaluetext)
        #断言存在District
        self.defineassertdetailstextnum(num, IndividuDetailsPage().district, IndividuDetailsPage().districttext)
        if districtinputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().districtvalue,districtinputtext)
        #断言存在Village
        self.defineassertdetailstextnum(num, IndividuDetailsPage().village, IndividuDetailsPage().villagetext)
        if villageinputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().villagevalue,villageinputtext)
        #断言存在Address
        self.defineassertdetailstextnum(num, IndividuDetailsPage().address, IndividuDetailsPage().addresstext)
        if addressinputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().addressvalue,addressinputtext)
        #断言存在Postcode
        self.defineassertdetailstextnum(num, IndividuDetailsPage().postcode, IndividuDetailsPage().postcodetext)
        if postcodeinputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().postcodevalue,postcodeinputtext)
        #断言存在Photo NPWP Company
        self.defineassertdetailstextnum(num, IndividuDetailsPage().photonpwpcompany, IndividuDetailsPage().photonpwpcompanytext)
        #断言存在Photo TDP
        self.defineassertdetailstextnum(num, IndividuDetailsPage().phototdp,IndividuDetailsPage().phototdptext)

        # 详情页存在Owner/Person in charge info
        self.defineassertdetailstextnum(num, IndividuDetailsPage().ownerpersoninchangeinfo, IndividuDetailsPage().ownerpersoninchangeinfotext)
        #断言存在Name
        self.defineassertdetailstextnum(num, IndividuDetailsPage().name, IndividuDetailsPage().nametext)
        self.defineassertdetailstextnum(num, IndividuDetailsPage().namevalue,nameinputtext)
        #断言存在NPWP
        self.defineassertdetailstextnum(num, IndividuDetailsPage().npwp, IndividuDetailsPage().npwptext)
        if npwpinputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().npwpvalue,npwpinputtext)
        #断言存在ID Type
        self.defineassertdetailstextnum(num, IndividuDetailsPage().typeid, IndividuDetailsPage().typeidtext)
        if typeidselectoptionxpath != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().typeidvalue,IndividuDetailsPage().typeidvaluetext)
        #断言存在Identity number
        self.defineassertdetailstextnum(num, IndividuDetailsPage().identitynumber, IndividuDetailsPage().identitynumbertext)
        if identitynumberinputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().identitynumbervalue,identitynumberinputtext)
        #断言存在Nationality
        self.defineassertdetailstextnum(num, IndividuDetailsPage().nationality, IndividuDetailsPage().nationalitytext)
        if nationalityselectoptionxpath != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().nationalityvalue,IndividuDetailsPage().nationalityvaluetext)
        #断言存在Phone
        self.defineassertdetailstextnum(num, IndividuDetailsPage().phone, IndividuDetailsPage().phonetext)
        if phoneinputtext !=None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().phonevalue,phoneinputtext)
        #断言存在Email2
        self.defineassertdetailstextnum(num, IndividuDetailsPage().email2, IndividuDetailsPage().email2text)
        if email2inputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().email2value,email2inputtext)
        #断言存在Address2
        self.defineassertdetailstextnum(num, IndividuDetailsPage().address2, IndividuDetailsPage().address2text)
        if address2inputtext != None:
            self.defineassertdetailstextnum(num, IndividuDetailsPage().address2value,address2inputtext)
        #断言存在Photo PIC Full-faceBust
        self.defineassertdetailstextnum(num, IndividuDetailsPage().photofullfacebust, IndividuDetailsPage().photofullfacebusttext)

        # 详情页存在Profile Photos
        self.defineassertdetailstextnum(num, IndividuDetailsPage().profilephotos, IndividuDetailsPage().profilephotostext)
        #断言存在Location Photo
        self.defineassertdetailstextnum(num, IndividuDetailsPage().locationphoto, IndividuDetailsPage().locationphototext)
        #断言存在Photo of the cashiers desk
        self.defineassertdetailstextnum(num, IndividuDetailsPage().photoofthecashiersdesk, IndividuDetailsPage().photoofthecashiersdesktext)
        #断言存在Other Photo
        self.defineassertdetailstextnum(num, IndividuDetailsPage().otherphoto, IndividuDetailsPage().otherphototext)












    def defineasserttextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在text:%s"%testtext)

    def defineassertdetailstextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        clicktext = ["Merchant info","Owner / Person in Charge info","Profile Photos"]
        if  expecttext in clicktext:
            self.activeweb.findElementByXpathAndScriptClickNum(num,testelexpath)
        self.assertEqual(expecttext,testtext)

    def defineisintable(self,num,testtablexpath,expecttext,tablecolnum):
        notexsitflag = True
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, testtablexpath)
        for value in tabledic.values():
            # self.activeweb.outPutMyLog("%s"% value[int(tablecolnum)])
            if str(expecttext).lower() in value[int(tablecolnum)].lower():
                self.assertTrue(True)
                self.activeweb.outPutMyLog("在%s中存在text:%s"% (value[int(tablecolnum)],expecttext))
                notexsitflag = False
                break
        if notexsitflag:
            self.activeweb.outPutMyLog("在%s不存在：%s"% (tabledic,expecttext))
            self.assertTrue(False)



    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc( num, isfictitious,brandnameinputtext, emailinputtext, contactnumberinputtext,  #添加个人商户
                          merchanttypeselectoptionxpath, categoryselectoptionxpath, criteriaselectoptionxpath,
                          siupinputtext, provinceselectoptionxpath, cityselectoptionxpath,
                          districtinputtext, villageinputtext, postcodeinputtext,addressinputtext,
                          photosiupimagefilepath, photonpwpcompanyimagefilepath, phototdpimagefilepath,
                          nameinputtext, npwpinputtext, typeidselectoptionxpath,
                          identitynumberinputtext, address2inputtext, nationalityselectoptionxpath,
                          phoneinputtext, email2inputtext, photofullfacebustimagefilepath,
                          locationphotoimagefilepath, photoofthecashiersdeskimagefilepath, otherphotoimagefilepath,
                          bankselectoptionxpath, accountnameinputtext, accountnumberinputtext,
                            qrindoaccountinputtext):
        def func(self):
            self.defineaddmerchantindividu(num, isfictitious,brandnameinputtext, emailinputtext, contactnumberinputtext,  #添加个人商户
                          merchanttypeselectoptionxpath, categoryselectoptionxpath, criteriaselectoptionxpath,
                          siupinputtext, provinceselectoptionxpath, cityselectoptionxpath,
                          districtinputtext, villageinputtext, postcodeinputtext,addressinputtext,
                          photosiupimagefilepath, photonpwpcompanyimagefilepath, phototdpimagefilepath,
                          nameinputtext, npwpinputtext, typeidselectoptionxpath,
                          identitynumberinputtext, address2inputtext, nationalityselectoptionxpath,
                          phoneinputtext, email2inputtext, photofullfacebustimagefilepath,
                          locationphotoimagefilepath, photoofthecashiersdeskimagefilepath, otherphotoimagefilepath,
                          bankselectoptionxpath, accountnameinputtext, accountnumberinputtext,
                          qrindoaccountinputtext)
        return func

def __generateTestCases():
    from addmerchant.models import AddMerchant

    addmerchant_all = AddMerchant.objects.filter(iscompany=False).filter(id=1).order_by('id')
    rows_count = addmerchant_all.count()

    for addmerchant in addmerchant_all:

        if len(str(addmerchant.id)) == 1:
            addmerchantid = '0000%s'% addmerchant.id
        elif len(str(addmerchant.id)) == 2:
            addmerchantid = '000%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 3:
            addmerchantid = '00%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 4:
            addmerchantid = '0%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 5:
            addmerchantid = '%s' % addmerchant.id
        else:
            addmerchantid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(addmerchant.id)
        args.append(addmerchant.isfictitious)
        args.append("%s_%s"%(addmerchant.brandnameinputtext,GetTimeStr().getTimeStr()))
        args.append(addmerchant.emailinputtext)
        args.append(addmerchant.contactnumberinputtext)
        args.append(addmerchant.merchanttypeselectoptionxpath)
        args.append(addmerchant.categoryselectoptionxpath)
        args.append(addmerchant.criteriaselectoptionxpath)
        args.append(addmerchant.siupinputtext)
        args.append(addmerchant.provinceselectoptionxpath)
        args.append(addmerchant.cityselectoptionxpath)
        args.append(addmerchant.districtinputtext)
        args.append(addmerchant.villageinputtext)
        args.append(addmerchant.postcodeinputtext)
        args.append(addmerchant.addressinputtext)
        args.append(addmerchant.photosiupimagefilepath)
        args.append(addmerchant.photonpwpcompanyimagefilepath)
        args.append(addmerchant.phototdpimagefilepath)
        args.append(addmerchant.nameinputtext)
        args.append(addmerchant.npwpinputtext)
        args.append(addmerchant.typeidselectoptionxpath)
        args.append(addmerchant.identitynumberinputtext)
        args.append(addmerchant.address2inputtext)
        args.append(addmerchant.nationalityselectoptionxpath)
        args.append(addmerchant.phoneinputtext)
        args.append(addmerchant.email2inputtext)
        args.append(addmerchant.photofullfacebustimagefilepath)
        args.append(addmerchant.locationphotoimagefilepath)
        args.append(addmerchant.photoofthecashiersdeskimagefilepath)
        args.append(addmerchant.otherphotoimagefilepath)
        args.append(addmerchant.bankselectoptionxpath)
        args.append(addmerchant.accountnameinputtext)
        args.append(addmerchant.accountnumberinputtext)
        args.append(addmerchant.qrindoaccountinputtext)


        setattr(TestAddMerchantClass, 'test_func_%s_%s' % (addmerchantid,addmerchant.testcasetitle),
                TestAddMerchantClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










