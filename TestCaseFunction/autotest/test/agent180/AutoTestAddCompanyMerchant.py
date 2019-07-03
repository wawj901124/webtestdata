import unittest

from webtestdata.settings import WEB_URL_TITLE,AGENT_LOGIN_ACCOUNT,AGENT_LOGIN_PASSWORD


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
from TestCaseFunction.autotest.config.page.agent180.addCompanyMerchantPage import AddCompanyMerchantPage
from TestCaseFunction.autotest.config.page.agent180.addMerchantSuccessPage import AddMerchantSuccessPage
from TestCaseFunction.autotest.config.page.agent180.addMerchantDonePage import AddMerchantDonePage
from TestCaseFunction.autotest.config.page.agent180.merchantListPage import MerchantListPage
from TestCaseFunction.autotest.config.page.agent180.companyDetailsPage import CompanyDetailsPage



class TestAddCompanyMerchantClass(unittest.TestCase):  # 创建测试类


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
        self.activeweb.findElementByXpathAndInput(LoginPage().account,AGENT_LOGIN_ACCOUNT)
        self.activeweb.findElementByXpathAndInput(LoginPage().password,AGENT_LOGIN_PASSWORD)
        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = AddCompanyMerchantPage()
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
        self.testpagecompanynameinput = self.testpage.companynameinput   #新加
        self.testpageofficialwebsiteinput = self.testpage.officialwebsiteinput   #新加
        self.testpagenpwptaxidinput = self.testpage.npwptaxidinput   #新加
        self.testpagephotosiupimage = self.testpage.photosiupimage   #更换
        self.testpagephotonpwpcompanyimage = self.testpage.photonpwpcompanyimage   #更换
        self.testpagephototdpimage = self.testpage.phototdpimage   #更换
        self.testpageownerpersoninchargeinfo = self.testpage.ownerpersoninchangeinfo #Owner / Person in Charge info中 元素
        self.testpagenameinput = self.testpage.nameinput
        self.testpagepositioninput = self.testpage.positioninput   #新加
        # self.testpagenpwpinput = self.testpage.npwpinput   #去掉
        # self.testpagetypeidselect = self.testpage.typeidselect   #去掉
        # self.testpageidentitynumberinput = self.testpage.identitynumberinput   #去掉
        # self.testpageaddress2input = self.testpage.address2input   #去掉
        # self.testpagenationalityselect = self.testpage.nationalityselect   #去掉
        self.testpagephoneinput = self.testpage.phoneinput   #更换
        self.testpageemail2input = self.testpage.email2input   #更换
        self.testpagephotofullfacebustimage = self.testpage.photofullfacebustimage   #更换
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
    def defineaddmerchantcompany(self, num,isfictitious=False, brandnameinputtext=None, emailinputtext=None, contactnumberinputtext=None,  #添加公司商户
                          merchanttypeselectoptionxpath=None, categoryselectoptionxpath=None, criteriaselectoptionxpath=None,
                          siupinputtext=None, provinceselectoptionxpath=None, cityselectoptionxpath=None,
                          districtinputtext=None, villageinputtext=None, postcodeinputtext=None,addressinputtext=None,
                          companynameinputtext=None,officialwebsiteinputtext=None,npwptaxidinputtext=None,   #新加
                          photosiupimagefilepath=None, photonpwpcompanyimagefilepath=None, phototdpimagefilepath=None,   #更换xpath
                          nameinputtext=None,
                          positioninputtext=None,   #新加
                          # npwpinputtext=None, typeidselectoptionxpath=None,   #去掉
                          # identitynumberinputtext=None, address2inputtext=None, nationalityselectoptionxpath=None,   #去掉
                          phoneinputtext=None, email2inputtext=None, photofullfacebustimagefilepath=None,   #更换
                          locationphotoimagefilepath=None, photoofthecashiersdeskimagefilepath=None, otherphotoimagefilepath=None,
                          bankselectoptionxpath=None, accountnameinputtext=None, accountnumberinputtext=None,
                          qrindoaccountinputtext=None):
        # self.activeweb.writerCookies(self.cookie, LoginPage().pageurl,MerchantListPage().pageurl)
        if isfictitious:
            self.writexunicookie()
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #添加公司商户
        #添加Basic info
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagebrandnameinput, brandnameinputtext)   #输入Brand name
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageemailinput, emailinputtext)  #输入Email

        #添加Merchant info
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagemerchanttypeselect,merchanttypeselectoptionxpath)  # 选择Merchant type
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecategoryselect, categoryselectoptionxpath)   # 选择Category
        if criteriaselectoptionxpath != None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecriteriaselect,criteriaselectoptionxpath)  # 选择Criteria
        if provinceselectoptionxpath != None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpageprovinceselect,provinceselectoptionxpath)  # 选择Province
        if cityselectoptionxpath != None:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecityselect,cityselectoptionxpath)  # 选择City
        if districtinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagedistrictinput, districtinputtext)  # 输入District
        if villageinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagevillageinput,villageinputtext)  # 输入Village
        if postcodeinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagepostcodeinput, postcodeinputtext)  # 输入Postcode
        if addressinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpageaddressinput, addressinputtext)  # 输入Address
        if companynameinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagecompanynameinput,companynameinputtext)  # 输入Company name   #新加
        if officialwebsiteinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpageofficialwebsiteinput, officialwebsiteinputtext)  # 输入Official Website   #新加
        if npwptaxidinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagenpwptaxidinput, npwptaxidinputtext)  # 输入NPWP/TAX ID   #新加
        if photonpwpcompanyimagefilepath != None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotonpwpcompanyimage,photonpwpcompanyimagefilepath)  # 添加Photo NPWP Company图片   #更换
        if phototdpimagefilepath != None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephototdpimage,phototdpimagefilepath)  # 添加Photo TDP图片   #更换

        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpagemerchantinfo)  #点击Merchant info
        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageownerpersoninchargeinfo)  # 点击Owner / Person in Charge info

        #添加Owner / Person in Charge info
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagenameinput, nameinputtext)  # 输入Name
        if positioninputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num, self.testpagepositioninput, positioninputtext)  # 输入Position   #新加
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpagenpwpinput, npwpinputtext)  # 输入NPWP   #去掉
        # self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagetypeidselect,typeidselectoptionxpath)  # 选择Type ID   #去掉
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpageidentitynumberinput, identitynumberinputtext)  # 输入Identity number   #去掉
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpageaddress2input, address2inputtext)  # 输入Address   #去掉
        # self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagenationalityselect,nationalityselectoptionxpath)  # 选择Nationality   #去掉
        if  phoneinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpagephoneinput, phoneinputtext)  # 输入Phone   #更换
        if email2inputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num,self.testpageemail2input, email2inputtext)  # 输入Email   #更换
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotofullfacebustimage,photofullfacebustimagefilepath)  # 添加Photo Full-faceBust图片   #更换

        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageownerpersoninchargeinfo)  # 点击Owner / Person in Charge info
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpageprofilephotos)  # 点击Profile Photos

        #添加Profile Photos
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagelocationphotoimage,locationphotoimagefilepath)  # 添加Location Photo图片
        if photoofthecashiersdeskimagefilepath !=None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotoofthecashiersdeskimage,photoofthecashiersdeskimagefilepath)  # 添加Photo of the cashiers desk图片
        if otherphotoimagefilepath != None:
            self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpageotherphotoimage,otherphotoimagefilepath)  # 添加Other Photo图片

        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpageprofilephotos)  # 点击Profile Photos
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpagebankaccount)  # 点击Bank account

        #添加Bank account
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagebankselect,bankselectoptionxpath)  # 选择Bank
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageaccountnameinput, accountnameinputtext)  # 输入Account name
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageaccountnumberinput, accountnumberinputtext)  # 输入Account number

        # self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagebankaccount)  # 点击Bank account
        # self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageqrindoaccount)  # 点击QRindo account
        # 
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpageqrindoaccountinput, AGENT_LOGIN_ACCOUNT)  # 输入QRindo account
        # self.activeweb.findElementByXpathAndClickNum(num,self.testpagecheckbutton)   #点击check按钮

        #点击submit按钮
        self.activeweb.findElementByXpathAndClickNum(num,self.testpagesubmitbutton)  # 点击submit按钮
        # self.activeweb.delayTime(1000)

        #断言是否有“Success”
        # self.defineasserttextnum(num,AddMerchantSuccessPage().success,AddMerchantSuccessPage().successtext)
        # self.activeweb.findElementByXpathAndClickNum(num,AddMerchantSuccessPage().okbutton)

        #断言是否有“Done”
        self.defineasserttextnum(num, AddMerchantDonePage().done, AddMerchantDonePage().donetext)

        # 断言是否有“Waiting for approval”
        self.defineasserttextnum(num, AddMerchantDonePage().waitingforapproval, AddMerchantDonePage().waitingforapprovaltext)

        # 断言是否有brandnameinputtext（添加的商户名）
        self.defineasserttextnum(num, AddMerchantDonePage().merchantnamevalue, brandnameinputtext)


        self.activeweb.findElementByXpathAndClickNum(num,AddMerchantDonePage().merchantlistbutton)
        #断言商户列表中是否有新增加的商户名
        self.defineisintable(num,MerchantListPage().searchtableresult,brandnameinputtext,1)
        #点击商户列表新建商户的Detail进入商户详情页；
        self.activeweb.findElementByXpathAndClickNum(num, MerchantListPage().operation_waitingforreview_details)

        #断言详情页中的内容
        #详情页存在Basic info
        self.defineassertdetailstextnum(num,CompanyDetailsPage().basicinfo,CompanyDetailsPage().basicinfotext)
        #断言存在Merchant ID
        self.defineassertdetailstextnum(num,CompanyDetailsPage().merchantid,CompanyDetailsPage().merchantidtext)
        merchantid = self.activeweb.findElementByXpathAndReturnText(num, CompanyDetailsPage().merchantidvalue)   #获取merchantid
        self.activeweb.outPutMyLog("新建商户id：%s" % merchantid)
        # 保存merchantid
        filename = "merchantid.txt"
        GetTimeStr().writeText(filename, merchantid)
        #断言存在Login account
        self.defineassertdetailstextnum(num, CompanyDetailsPage().loginaccount, CompanyDetailsPage().loginaccounttext)
        self.defineassertdetailstextnum(num, CompanyDetailsPage().loginaccountvalue, emailinputtext)
        #断言存在Brand name
        self.defineassertdetailstextnum(num, CompanyDetailsPage().brandname, CompanyDetailsPage().brandnametext)
        self.defineassertdetailstextnum(num, CompanyDetailsPage().brandnamevalue,brandnameinputtext)
        #断言存在agent
        self.defineassertdetailstextnum(num,CompanyDetailsPage().agent,CompanyDetailsPage().agentvalue)

        # 详情页存在Merchant info
        self.defineassertdetailstextnum(num, CompanyDetailsPage().merchantinfo, CompanyDetailsPage().merchantinfotext)
        #断言存在Merchant type
        self.defineassertdetailstextnum(num, CompanyDetailsPage().merchanttype, CompanyDetailsPage().merchanttypetext)
        self.defineassertdetailstextnum(num, CompanyDetailsPage().merchanttypevalue,CompanyDetailsPage().merchanttypevaluetext)
        #断言存在Category
        self.defineassertdetailstextnum(num, CompanyDetailsPage().category, CompanyDetailsPage().categorytext)
        self.defineassertdetailstextnum(num, CompanyDetailsPage().categoryvalue,CompanyDetailsPage().categoryvaluetext)
        #断言存在Criteria
        self.defineassertdetailstextnum(num, CompanyDetailsPage().criteria, CompanyDetailsPage().criteriatext)
        if criteriaselectoptionxpath != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().criteriavalue,CompanyDetailsPage().criteriavaluetext)
        #断言存在Province
        self.defineassertdetailstextnum(num, CompanyDetailsPage().province, CompanyDetailsPage().provincetext)
        if provinceselectoptionxpath != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().provincevalue,CompanyDetailsPage().provincevaluetext)
        #断言存在City
        self.defineassertdetailstextnum(num, CompanyDetailsPage().city, CompanyDetailsPage().citytext)
        if cityselectoptionxpath !=None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().cityvalue,CompanyDetailsPage().cityvaluetext)
        #断言存在District
        self.defineassertdetailstextnum(num, CompanyDetailsPage().district, CompanyDetailsPage().districttext)
        if districtinputtext != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().districtvalue,districtinputtext)
        #断言存在Village
        self.defineassertdetailstextnum(num, CompanyDetailsPage().village, CompanyDetailsPage().villagetext)
        self.defineassertdetailstextnum(num, CompanyDetailsPage().villagevalue,villageinputtext)
        #断言存在Address
        self.defineassertdetailstextnum(num, CompanyDetailsPage().address, CompanyDetailsPage().addresstext)
        if addressinputtext != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().addressvalue,addressinputtext)
        #断言存在Postcode
        self.defineassertdetailstextnum(num, CompanyDetailsPage().postcode, CompanyDetailsPage().postcodetext)
        if postcodeinputtext != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().postcodevalue,postcodeinputtext)
        #断言存在Company name
        self.defineassertdetailstextnum(num, CompanyDetailsPage().companyname, CompanyDetailsPage().companynametext)   #公司专有
        if companynameinputtext != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().companynamevalue,companynameinputtext)   #公司专有
        #断言存在Official website
        self.defineassertdetailstextnum(num, CompanyDetailsPage().officialwebsite, CompanyDetailsPage().officialwebsitetext)   #公司专有
        if officialwebsiteinputtext !=None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().officialwebsitevalue,officialwebsiteinputtext)   #公司专有
        #断言存在NPWP / TAX ID
        self.defineassertdetailstextnum(num, CompanyDetailsPage().npwptaxid, CompanyDetailsPage().npwptaxidtext)   #公司专有
        if npwptaxidinputtext != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().npwptaxidvalue,npwptaxidinputtext)   #公司专有
        #断言存在Photo NPWP Company
        self.defineassertdetailstextnum(num, CompanyDetailsPage().photonpwpcompany, CompanyDetailsPage().photonpwpcompanytext)
        #断言存在Photo TDP
        self.defineassertdetailstextnum(num, CompanyDetailsPage().phototdp,CompanyDetailsPage().phototdptext)

        # 详情页存在Owner/Person in charge info
        self.defineassertdetailstextnum(num, CompanyDetailsPage().ownerpersoninchangeinfo, CompanyDetailsPage().ownerpersoninchangeinfotext)
        #断言存在Name
        self.defineassertdetailstextnum(num, CompanyDetailsPage().name, CompanyDetailsPage().nametext)
        self.defineassertdetailstextnum(num, CompanyDetailsPage().namevalue,nameinputtext)
        # #断言存在NPWP
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().npwp, CompanyDetailsPage().npwptext)   #个人专有
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().npwpvalue,npwpinputtext)   #个人专有
        # #断言存在ID Type
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().typeid, CompanyDetailsPage().typeidtext)   #个人专有
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().typeidvalue,CompanyDetailsPage().typeidvaluetext)   #个人专有
        # #断言存在Identity number
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().identitynumber, CompanyDetailsPage().identitynumbertext)   #个人专有
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().identitynumbervalue,identitynumberinputtext)   #个人专有
        # #断言存在Nationality
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().nationality, CompanyDetailsPage().nationalitytext)   #个人专有
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().nationalityvalue,CompanyDetailsPage().nationalityvaluetext)   #个人专有
        #断言存在Phone
        self.defineassertdetailstextnum(num, CompanyDetailsPage().phone, CompanyDetailsPage().phonetext)
        if phoneinputtext != None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().phonevalue,phoneinputtext)
        #断言存在Email2
        self.defineassertdetailstextnum(num, CompanyDetailsPage().email2, CompanyDetailsPage().email2text)
        if email2inputtext !=None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().email2value,email2inputtext)
        # #断言存在Address2
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().address2, CompanyDetailsPage().address2text)   #个人专有
        # self.defineassertdetailstextnum(num, CompanyDetailsPage().address2value,address2inputtext)   #个人专有
        #断言存在Position
        self.defineassertdetailstextnum(num, CompanyDetailsPage().position, CompanyDetailsPage().positiontext)   #公司专有
        if positioninputtext !=None:
            self.defineassertdetailstextnum(num, CompanyDetailsPage().positionvalue,positioninputtext)   #公司专有
        #断言存在Photo PIC Full-faceBust
        self.defineassertdetailstextnum(num, CompanyDetailsPage().photofullfacebust, CompanyDetailsPage().photofullfacebusttext)

        # 详情页存在Profile Photos
        self.defineassertdetailstextnum(num, CompanyDetailsPage().profilephotos, CompanyDetailsPage().profilephotostext)
        #断言存在Location Photo
        self.defineassertdetailstextnum(num, CompanyDetailsPage().locationphoto, CompanyDetailsPage().locationphototext)
        #断言存在Photo of the cashiers desk
        self.defineassertdetailstextnum(num, CompanyDetailsPage().photoofthecashiersdesk, CompanyDetailsPage().photoofthecashiersdesktext)
        #断言存在Other Photo
        self.defineassertdetailstextnum(num, CompanyDetailsPage().otherphoto, CompanyDetailsPage().otherphototext)
        
        

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
    def getTestFunc(num, isfictitious,brandnameinputtext, emailinputtext, contactnumberinputtext,  #添加公司商户
                    merchanttypeselectoptionxpath, categoryselectoptionxpath, criteriaselectoptionxpath,
                    siupinputtext, provinceselectoptionxpath, cityselectoptionxpath,
                    districtinputtext, villageinputtext, postcodeinputtext, addressinputtext,
                    companynameinputtext, officialwebsiteinputtext, npwptaxidinputtext,  # 新加
                    photosiupimagefilepath, photonpwpcompanyimagefilepath, phototdpimagefilepath,  #更换xpath
                    nameinputtext,
                    positioninputtext,  # 新加
                    # npwpinputtext, typeidselectoptionxpath,   #去掉
                    # identitynumberinputtext, address2inputtext, nationalityselectoptionxpath,   #去掉
                    phoneinputtext, email2inputtext, photofullfacebustimagefilepath,   #更换
                    locationphotoimagefilepath, photoofthecashiersdeskimagefilepath, otherphotoimagefilepath,
                    bankselectoptionxpath, accountnameinputtext, accountnumberinputtext,
                    qrindoaccountinputtext):
        def func(self):
            self.defineaddmerchantcompany(num,isfictitious,brandnameinputtext, emailinputtext, contactnumberinputtext,  #添加公司商户
                          merchanttypeselectoptionxpath, categoryselectoptionxpath, criteriaselectoptionxpath,
                          siupinputtext, provinceselectoptionxpath, cityselectoptionxpath,
                          districtinputtext, villageinputtext, postcodeinputtext,addressinputtext,
                          companynameinputtext, officialwebsiteinputtext, npwptaxidinputtext,  # 新加
                          photosiupimagefilepath, photonpwpcompanyimagefilepath, phototdpimagefilepath,  #更换xpath
                          nameinputtext,
                          positioninputtext,  # 新加
                          # npwpinputtext, typeidselectoptionxpath,   #去掉
                          # identitynumberinputtext, address2inputtext, nationalityselectoptionxpath,   #去掉
                          phoneinputtext, email2inputtext, photofullfacebustimagefilepath,
                          locationphotoimagefilepath, photoofthecashiersdeskimagefilepath, otherphotoimagefilepath,
                          bankselectoptionxpath, accountnameinputtext, accountnumberinputtext,
                          qrindoaccountinputtext)
        return func

def __generateTestCases():
    from addmerchant.models import AddMerchant

    addmerchant_all = AddMerchant.objects.filter(iscompany=True).filter(id=2).order_by('id')
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
        args.append(addmerchant.companynameinputtext)  # 新加
        args.append(addmerchant.officialwebsiteinputtext)  # 新加
        args.append(addmerchant.npwptaxidinputtext)  # 新加
        args.append(addmerchant.photosiupimagefilepath)   #更换
        args.append(addmerchant.photonpwpcompanyimagefilepath)   #更换
        args.append(addmerchant.phototdpimagefilepath)   #更换
        args.append(addmerchant.nameinputtext)
        args.append(addmerchant.positioninputtext)   # 新加
        # args.append(addmerchant.npwpinputtext)   #去掉
        # args.append(addmerchant.typeidselectoptionxpath)   #去掉
        # args.append(addmerchant.identitynumberinputtext)   #去掉
        # args.append(addmerchant.address2inputtext)   #去掉
        # args.append(addmerchant.nationalityselectoptionxpath)   #去掉
        args.append(addmerchant.phoneinputtext)   #更换
        args.append(addmerchant.email2inputtext)   #更换
        args.append(addmerchant.photofullfacebustimagefilepath)   #更换
        args.append(addmerchant.locationphotoimagefilepath)
        args.append(addmerchant.photoofthecashiersdeskimagefilepath)
        args.append(addmerchant.otherphotoimagefilepath)
        args.append(addmerchant.bankselectoptionxpath)
        args.append(addmerchant.accountnameinputtext)
        args.append(addmerchant.accountnumberinputtext)
        args.append(addmerchant.qrindoaccountinputtext)


        setattr(TestAddCompanyMerchantClass, 'test_func_%s_%s' % (addmerchantid,addmerchant.testcasetitle),
                TestAddCompanyMerchantClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










