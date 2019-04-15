import unittest

from webtestdata.settings import WEB_URL_TITLE


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson

from autotest.config.page.agent.loginPage import LoginPage
from autotest.config.page.agent.addCompanyMerchantPage import AddCompanyMerchantPage


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
        self.activeweb.findElementByXpathAndInput(LoginPage().account,"81122336666")
        self.activeweb.findElementByXpathAndInput(LoginPage().password,"abc123456")
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

    #定义搜索查找函数
    def defineaddmerchantcompany(self, num, brandnameinputtext=None, emailinputtext=None, contactnumberinputtext=None,  #添加公司商户
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
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #添加个人商户
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagebrandnameinput, brandnameinputtext)   #输入Brand name
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageemailinput, emailinputtext)  #输入Email
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagecontactnumberinput, contactnumberinputtext)   #输入Contact number
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagemerchanttypeselect,merchanttypeselectoptionxpath)  # 选择Merchant type
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecategoryselect, categoryselectoptionxpath)   # 选择Category
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecriteriaselect,criteriaselectoptionxpath)  # 选择Criteria
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagesiupinput, siupinputtext)  # 输入SIUP
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpageprovinceselect,provinceselectoptionxpath)  # 选择Province
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagecityselect,cityselectoptionxpath)  # 选择City
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagedistrictinput, districtinputtext)  # 输入District
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagevillageinput,villageinputtext)  # 输入Village
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagepostcodeinput, postcodeinputtext)  # 输入Postcode
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageaddressinput, addressinputtext)  # 输入Address
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagecompanynameinput,companynameinputtext)  # 输入Company name   #新加
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageofficialwebsiteinput, officialwebsiteinputtext)  # 输入Official Website   #新加
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagenpwptaxidinput, npwptaxidinputtext)  # 输入NPWP/TAX ID   #新加

        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotosiupimage, photosiupimagefilepath) #添加Photo SIUP图片   #更换
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotonpwpcompanyimage,photonpwpcompanyimagefilepath)  # 添加Photo NPWP Company图片   #更换
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephototdpimage,phototdpimagefilepath)  # 添加Photo TDP图片   #更换

        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpagemerchantinfo)  #点击Merchant info
        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageownerpersoninchargeinfo)  # 点击Owner / Person in Charge info

        self.activeweb.findElementByXpathAndInputNum(num,self.testpagenameinput, nameinputtext)  # 输入Name
        self.activeweb.findElementByXpathAndInputNum(num, self.testpagepositioninput, positioninputtext)  # 输入Position   #新加

        # self.activeweb.findElementByXpathAndInputNum(num,self.testpagenpwpinput, npwpinputtext)  # 输入NPWP   #去掉
        # self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagetypeidselect,typeidselectoptionxpath)  # 选择Type ID   #去掉
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpageidentitynumberinput, identitynumberinputtext)  # 输入Identity number   #去掉
        # self.activeweb.findElementByXpathAndInputNum(num,self.testpageaddress2input, address2inputtext)  # 输入Address   #去掉
        # self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagenationalityselect,nationalityselectoptionxpath)  # 选择Nationality   #去掉
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagephoneinput, phoneinputtext)  # 输入Phone   #更换
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageemail2input, email2inputtext)  # 输入Email   #更换
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotofullfacebustimage,photofullfacebustimagefilepath)  # 添加Photo Full-faceBust图片   #更换

        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageownerpersoninchargeinfo)  # 点击Owner / Person in Charge info
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpageprofilephotos)  # 点击Profile Photos

        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagelocationphotoimage,locationphotoimagefilepath)  # 添加Location Photo图片
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpagephotoofthecashiersdeskimage,photoofthecashiersdeskimagefilepath)  # 添加Photo of the cashiers desk图片
        self.activeweb.findElementByXpathAndAndFileNumVue(num,self.testpageotherphotoimage,otherphotoimagefilepath)  # 添加Other Photo图片

        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpageprofilephotos)  # 点击Profile Photos
        self.activeweb.findElementByXpathAndScriptClickNum(num,self.testpagebankaccount)  # 点击Bank account

        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagebankselect,bankselectoptionxpath)  # 选择Bank
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageaccountnameinput, accountnameinputtext)  # 输入Account name
        self.activeweb.findElementByXpathAndInputNum(num,self.testpageaccountnumberinput, accountnumberinputtext)  # 输入Account number

        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagebankaccount)  # 点击Bank account
        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpageqrindoaccount)  # 点击QRindo account

        self.activeweb.findElementByXpathAndInputNum(num,self.testpageqrindoaccountinput, qrindoaccountinputtext)  # 输入QRindo account
        self.activeweb.findElementByXpathAndClickNum(num,self.testpagecheckbutton)   #点击check按钮

        self.activeweb.findElementByXpathAndClickNum(num,self.testpagesubmitbutton)  # 点击submit按钮
        self.activeweb.delayTime(1000)
        # self.activeweb.findElementByXpathAndClickNum(num,self.testpageresetbutton)  # 点击reset按钮

        # def test_02(self):  # 添加公司商户
        #     """
        #     添加页面元素
        #     :return:
        #     """
        #     self.addmerchantpage = self.addmerchantpagecompany
        #     writebrandname = "123456"
        #     writeremail = "xiangkaizheng@iapppay.com"
        #     writercontactnumber = "abc123456"
        #     writermerchanttype = "Company"
        #     writercategory = "TAXICABS & LIMOUSINES"
        #     writercriteria = "Medium"
        #     writersiup = "abc123456"
        #     writerprovince = "JAMBI"
        #     writercity = "Kab. Bungo"
        #     writerdistrict = "abc123456"
        #     writervillage = "abc123456"
        #     writerpostcode = "abc123456"
        #     writeraddress = "abc123456"
        #     writercompany = "abc123456"
        #     writernpwptaxid = "abc123456"
        #     writerofficialwebsite = "abc123456"
        #     writerphotosiup = "D:\\pic\\1.png"
        #     writerphotonpwpcompany = "D:\\pic\\1.png"
        #     writerphototdp = "D:\\pic\\1.png"
        #
        #     writername = "abc123456"
        #     writerposition = "abc123456"
        #     writerphone = "abc123456"
        #     writeremailtwo = "xiangkaizheng@iapppay.com"
        #     writerphotofullfacebust = "D:\\pic\\1.png"
        #
        #     writerlocationphoto = "D:\\pic\\1.png"
        #     writerphotoofthecashiersdesk = "D:\\pic\\1.png"
        #     writerotherphoto = "D:\\pic\\1.png"
        #
        #     writerbank = "BCA"
        #     writeraccountname = "abc123456"
        #     writeraccountnumber = "abc123456"
        #
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.brandnameinput, writebrandname)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailinput, writeremail)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.contactnumberinput, writercontactnumber)
        #     self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.merchanttypeselect,
        #                                                       writermerchanttype)
        #     self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.categoryselect, writercategory)
        #     self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.criteriaselect, writercriteria)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.siupinput, writersiup)
        #     self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.provinceselect, writerprovince)
        #     self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.cityselect, writercity)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.districtinput, writerdistrict)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.villageinput, writervillage)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.postcodeinput, writerpostcode)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.addressinput, writeraddress)
        #
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.companyinput, writercompany)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.officialwebsiteinput, writerofficialwebsite)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.npwptaxidinput, writernpwptaxid)
        #
        #     self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photosiupimage, writerphotosiup)
        #     self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photonpwpcompanyimage,
        #                                                 writerphotonpwpcompany)
        #     self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.phototdpimage, writerphototdp)
        #
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.nameinput, writername)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.positioninput, writerposition)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.phoneinput, writerphone)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailtwoinput, writeremailtwo)
        #     self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photofullfacebustimage,
        #                                                 writerphotofullfacebust)
        #
        #     self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.locationphotoimage, writerlocationphoto)
        #     self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photoofthecashiersdeskimage,
        #                                                 writerphotoofthecashiersdesk)
        #     self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.otherphotoimage, writerotherphoto)
        #
        #     self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.bankselect, writerbank)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnameinput, writeraccountname)
        #     self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnumberinput, writeraccountnumber)
        #
        #     self.activeweb.findElementByXpathAndClick(self.addmerchantpage.submitbutton)
        #     self.activeweb.delayTime(3)
        #     self.activeweb.findElementByXpathAndClick(self.addmerchantdonepage.merchantlistbutton)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num, brandnameinputtext, emailinputtext, contactnumberinputtext,  #添加公司商户
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
            self.defineaddmerchantcompany(num,brandnameinputtext, emailinputtext, contactnumberinputtext,  #添加公司商户
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

    addmerchant_all = AddMerchant.objects.filter(iscompany=True).order_by('id')
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
        args.append(addmerchant.brandnameinputtext)
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










