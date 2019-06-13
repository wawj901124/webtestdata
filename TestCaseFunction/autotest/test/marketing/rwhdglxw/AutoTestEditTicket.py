import unittest

from webtestdata.settings import WEB_URL_TITLE,MANAGER_LOGIN_ACCOUNT,MANAGER_LOGIN_PASSWORD


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson
from TestCaseFunction.util.gettimestr import GetTimeStr

from TestCaseFunction.autotest.config.page.manager.loginPage import LoginPage   #导入登录页
from TestCaseFunction.autotest.config.page.marketing.rwhdglxw.activityCreatePage import ActivityCreatePage   #导入创建活动页
from TestCaseFunction.autotest.config.page.marketing.rwhdglxw.activityEditPage import ActivityEditPage  #导入未上线活动编辑页
from TestCaseFunction.autotest.config.page.marketing.rwhdglxw.ticketCreatePage import TicketCreatePage   #导入创建优惠券页
from TestCaseFunction.autotest.config.page.marketing.rwhdglxw.activityListPage import ActivityListPage   #导入活动列表页
from TestCaseFunction.autotest.config.page.marketing.rwhdglxw.ticketEditPage import TicketEditPage #导入未上线活动优惠券编辑页


class TestEditTicketClass(unittest.TestCase):  # 创建测试类

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
        self.activeweb.findElementByXpathAndInput(LoginPage().account,MANAGER_LOGIN_ACCOUNT)
        self.activeweb.findElementByXpathAndInput(LoginPage().password,MANAGER_LOGIN_PASSWORD)
        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)

        self.testpage = TicketEditPage()
        self.testpageurl =self.testpage.pageurl   #测试页面url
        self.testpagekcslinput  = self.testpage.kcsl_input   #第一部分# 库存数量输入框路径
        self.testpageqyxqselect = self.testpage.qyxq_select   #第一部分# 券有效期选择框路径
        self.testpageyhqsmareatext  = self.testpage.yhqsm_areatext    #第一部分# 优惠券说明多行输入框路径
        self.testpageyhqmcinput = self.testpage.yhqmc_input    #第二部分# 优惠券名称输入框路径
        self.testpageyhlxselect = self.testpage.yhlx_select    #第二部分# 优惠类型选择框路径
        self.testpageyhmsselect = self.testpage.yhms_select    #第二部分# 优惠模式选择框路径
        self.testpagezdxfinput = self.testpage.zdxf_input    #第二部分# 最低消费输入框路径
        self.testpagezfqdxzselect  = self.testpage.zfqdxz_select     #第二部分# 支付渠道限制选择框路径
        self.testpagesyfwselect   = self.testpage.syfw_select     #第二部分# 使用范围选择框路径

        self.testpagecancelbutton = self.testpage.cancel_button # 页面取消按钮
        self.testpageconfirmbutton = self.testpage.confirm_button  # 页面确定按钮

        ######################编辑活动页面###############################
        self.activityeditpage = ActivityEditPage()
        self.activityeditpage_pageurl = self.activityeditpage.pageurl
        self.activityeditpage_w_tjlp = self.activityeditpage.w_tjlp    # ---活动奖励---# 未添加礼品时，“添加礼品”文字链接路径

        #pass
        ######################活动列表页###############################
        self.activitylistpage = ActivityListPage()   #活动列表页
        self.activitylistpage_searchtableresult = self.activitylistpage.searchtableresult


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    def writexunicookie(self):
        addcookie = {'name': '.nereus.manager.settle.banks', 'value': 'QCK9GvKG8OEOh6lRUyyLlmKnHl8i3w'}
        self.activeweb.driver.add_cookie(addcookie)
        self.activeweb.driver.refresh()
        self.activeweb.delayTime(5)
        self.activeweb.outPutMyLog("写入虚拟银行cookie完成")

    #定义创建活动,
    #发放状态为1表示开启，否则为关闭
    #券有效期为1表示相对时间，否则为绝对时间
    #营销成本承担方为1表示平台，否则为商户
    #优惠类型为1表示代金券
    #优惠模式为1表示固定金额，否则为随机金额
    #支付渠道限制为1表示不限，为2表示钱包余额，为3表示银行卡支付
    #使用平台为0表示两个都点选，1表示点选QRindo，为2表示点选PaySDK
    #使用范围为1表示不限，为2表示指定行业，为3表示指定商户
    #是否支持退券为1表示可退，为2表示不可退

    def definecreateticket(self,num,ffzt,kcslinputtext,qyxq,
                           xdsjtsinputtext,
                           yxcbcdf,yhqmcinputtext,yhlx,
                           yhms,gdjemzinputtext,sjjemzmiminputtext,sjjemzmimaxinputtext,
                           zdxfinputtext,sypt,
                           syfw,zdhyoptionxpath,zdshinputtext,isplsh,plfilepath,
                           kfyqthddj,
                           sfzctq,iscancel):
        self.activeweb.getUrl(self.activityeditpage_pageurl)
        self.activeweb.delayTime(3)
        #创建活动
        #填入基础信息部分
        self.activeweb.findElementByXpathAndInputNum(num,self.activityeditpage.hdmc_input, yhqmcinputtext)   #输入活动名称
        self.activeweb.findElementByXpathAndClickAbountData(num,self.activityeditpage.hdsj_starttime,self.activityeditpage.hdsj_starttime_daytime,pathright=self.activityeditpage.hdsj_starttime_rightmove,pathconfirm=self.activityeditpage.hdsj_starttime_queding)   #点选活动时间开始时间
        self.activeweb.findElementByXpathAndClickAbountData(num,self.activityeditpage.hdsj_endtime ,self.activityeditpage.hdsj_endtime_daytime,pathright=self.activityeditpage.hdsj_endtime_rightmove,pathconfirm=self.activityeditpage.hdsj_endtime_queding)   #点选活动时间结束时间
        self.activeweb.findElementByXpathAndInputNum(num,self.activityeditpage.hdys_input, "2000")   #输入活动预算

        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.activityeditpage.tfqd_select,self.activityeditpage.tfqd_select_nbqd_option)  # 投放渠道一级渠道选择内部渠道

        # 点选投放渠道二级渠道全部项复选框
        self.activeweb.findElementByXpathAndClickNum(num, self.activityeditpage.tfqd_select_nbqd_fxk_mbmpay_checkbox)

        #填入活动任务规则部分
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.activityeditpage.rwlx_select,self.activityeditpage.rwlx_select_zc_option)  # 任务类型选择注册


        #编辑活动页，点击奖励礼品列表中的“edit”进入券编辑页
        self.activeweb.findElementByXpathAndClickNum(num, self.activityeditpage.y_jllp_table_cz_just_one_edit)  # 点击只有一个奖品时，奖品对应的编辑

        #进入创建优惠券页，新建优惠券
        #第一部分
        if ffzt == "1":
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.ffzt_kq_checkbox)  # 点击发放状态开始对应的选项框
        else:
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.ffzt_gb_checkbox)  # 点击发放状态关闭对应的选项框
        if kcslinputtext !=None:
            self.activeweb.findElementByXpathAndInputNum(num, self.testpagekcslinput,kcslinputtext) # 输入库存数量
        if qyxq == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpageqyxqselect,self.testpage.qyxq_select_option_xdsj)  # 选择券有效期选项为相对时间
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.qyxq_select_option_xdsj_ts_input, xdsjtsinputtext)  # 输入相对时间
        else:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpageqyxqselect,self.testpage.qyxq_select_option_jdsj)  # 选择券有效期选项为绝对时间
            self.activeweb.findElementByXpathAndClickAbountData(num, self.testpage.qyxq_select_option_jdsj_starttime,self.testpage.qyxq_select_option_jdsj_starttime_daytime,
                                                                pathright=self.testpage.qyxq_select_option_jdsj_starttime_pathright)  # 点选活动时间开始时间
            self.activeweb.findElementByXpathAndClickAbountData(num, self.testpage.qyxq_select_option_jdsj_endtime,self.testpage.qyxq_select_option_jdsj_endtime_daytime,
                                                                pathright=self.testpage.qyxq_select_option_jdsj_endtime_pathright)  # 点选活动时间结束时间
        if yxcbcdf == "1":
             self.activeweb.findElementByXpathAndClickNum(num, self.testpage.yxcbcdf_pt_checkbox)  # 点击营销成本承担方中的平台前的选项框
        else:
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.yxcbcdf_sh_checkbox)  # 点击营销成本承担方中的商户前的选项框

        self.activeweb.findElementByXpathAndInputNum(num, self.testpageyhqsmareatext,
        "%s（发放状态为1表示开启，否则为关闭）- 库存数量：【%s】-%s(券有效期为1表示相对时间(相对天数：【%s】)，否则为绝对时间)-%s（营销成本承担方为1表示平台，否则为商户）-%s（优惠类型为1表示代金券）-%s（优惠模式为1表示固定金额，否则为随机金额）-（1-面值:【%s】;2-面值最小值为：【%s】,最大值为：【%s】）-最低消费：【%s】-%s（使用平台为1表示QRindo，为2表示PaySDK）-%s（使用范围为1表示不限，为2表示指定行业，为3表示指定商户）-%s(是否支持退券为1表示可退，为2表示不可退)"
                                                     % (ffzt,kcslinputtext,qyxq,xdsjtsinputtext,yxcbcdf,yhlx,yhms,gdjemzinputtext,sjjemzmiminputtext,
                                                        sjjemzmimaxinputtext,zdxfinputtext,sypt,syfw,sfzctq))  # 输入优惠券说明
        #第二部分
        self.activeweb.findElementByXpathAndInputNum(num, self.testpageyhqmcinput,yhqmcinputtext)  # 添加优惠券名称
        if yhlx == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpageyhlxselect,self.testpage.yhlx_option_djq)   #优惠类型选择代金券

        if yhms == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpageyhmsselect,self.testpage.yhms_select_option_gdje)   #优惠模式选择固定金额
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.yhms_select_option_gdje_mz_input,gdjemzinputtext)  # 面值输入
        else:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpageyhmsselect,self.testpage.yhms_select_option_sjje)  # 优惠模式选择随机金额
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.yhms_select_option_sjje_mz_min_input,sjjemzmiminputtext)  # 面值最小值输入
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.yhms_select_option_sjje_mz_max_input,sjjemzmimaxinputtext)  # 面值最大值输入
        if zdxfinputtext != None:
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.zdxf_input,zdxfinputtext) # 输入最低消费金额

        if sypt == "0":
            self.activeweb.findElementByXpathAndClickNum(num,self.testpage.sypt_QRindo_checkbox)  # 使用平台点选QRindo
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.sypt_PaySDK_checkbox)  # 使用平台点选PaySDK
        elif sypt == "1":
            self.activeweb.findElementByXpathAndClickNum(num,self.testpage.sypt_QRindo_checkbox)  # 使用平台点选QRindo
        elif sypt == "2":
            self.activeweb.findElementByXpathAndClickNum(num,self.testpage.sypt_PaySDK_checkbox)  # 使用平台点选PaySDK

        if syfw == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagesyfwselect,self.testpage.syfw_select_option_bx)   #使用范围选择不限
        elif syfw == "2":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagesyfwselect,self.testpage.syfw_select_option_zdhy)   #使用范围选择指定行业
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpage.syfw_select_option_zdhy_select,self.testpage.syfw_select_option_zdhy_select_option_one) # 指定行业选择一个行业
            self.activeweb.findElementByXpathAndClickNum(num,
                                                         self.testpage.syfw_select_option_zdhy_select)  # 再次点击指定行业选择框
        elif syfw == "3":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagesyfwselect,self.testpage.syfw_select_option_zdsh)   #使用范围选择指定商户
            if isplsh:
                self.activeweb.findElementByXpathAndAndFileNumVue(num,
                                                             self.testpage.syfw_select_option_zdsh_pltjsh_button,plfilepath)  # 点击批量添加商户批量导入文件
            else:
                self.activeweb.findElementByXpathAndInputNum(num, self.testpage.syfw_select_option_zdsh_input,zdshinputtext)  # 输入商户
                self.activeweb.delayTime(3)
                self.activeweb.findElementByXpathAndClickNum(num,
                                                             self.testpage.syfw_select_option_zdsh_input_option_one)  # 点击商户输入框下拉列表第一项
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.syfw_select_option_zdsh_tjsh_button)  # 点击添加商户按钮

        # self.activeweb.delayTime(5000)

        if syfw == "1": #使用范围选择不限
            if kfyqthddj == "1":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.kfyqthddj_bkdjsy_checkbox)  # 是否与其他活动叠加，点选不可叠加使用
            elif sfzctq == "2":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.kfyqthddj_kydjsy_checkbox)  # 是否与其他活动叠加，点选可以叠加使用
            if sfzctq == "1":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.sfzctq_kt_checkbox)  # 是否支持退券点选可退
            elif sfzctq == "2":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.sfzctq_bkt_checkbox)  # 是否支持退券点选不可退

            if iscancel:
                self.activeweb.findElementByXpathAndClickNum(num, self.testpagecancelbutton)  # 点击取消按钮
                self.activeweb.findElementByXpathAndReturnText(num,self.activityeditpage.w_tjlp) #确保有添加礼品按钮
            else:
                self.activeweb.findElementByXpathAndClickNum(num, self.testpageconfirmbutton)  # 点击确定按钮
                # 断言添加礼品列表中是否有新增加的礼品
                self.defineisintable(num, self.activityeditpage.y_jllp_table, yhqmcinputtext, 1)
        else: #使用范围选择指定行业或者指定商户
            if kfyqthddj == "1":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.kfyqthddj_bkdjsy_checkbox_zdhy)  # 是否与其他活动叠加，点选不可叠加使用
            elif sfzctq == "2":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.kfyqthddj_kydjsy_checkbox_zdhy)  # 是否与其他活动叠加，点选可以叠加使用
            if sfzctq == "1":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.sfzctq_kt_checkbox_zdhy)  # 是否支持退券点选可退
            elif sfzctq == "2":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.sfzctq_bkt_checkbox_zdhy)  # 是否支持退券点选不可退

            if iscancel:
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.cancel_button_zdsh)  # 点击取消按钮
                self.activeweb.findElementByXpathAndReturnText(num, self.activityeditpage.w_tjlp)  #确保有添加礼品按钮
            else:
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.confirm_button_zdsh)  # 点击确定按钮
                # 断言添加礼品列表中是否有新增加的礼品
                self.defineisintable(num, self.activityeditpage.y_jllp_table, yhqmcinputtext, 1)
        ################################优惠券编辑完成#########################################

        if iscancel:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.activityeditpage.cancelbutton)  # 点击取消按钮
        else:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.activityeditpage.submitbutton)  # 点击提交按钮
            # 断言活动列表中是否有新增加的活动
            self.defineisintable(num, self.activitylistpage_searchtableresult,yhqmcinputtext , 1)


    def defineasserttextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在text:%s"%testtext)

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
    def getTestFunc(num,ffzt,kcslinputtext,qyxq,
                           xdsjtsinputtext,
                           yxcbcdf,yhqmcinputtext,yhlx,
                           yhms,gdjemzinputtext,sjjemzmiminputtext,sjjemzmimaxinputtext,
                           zdxfinputtext,sypt,
                           syfw,zdhyoptionxpath,zdshinputtext,isplsh,plfilepath,
                           kfyqthddj,
                           sfzctq,iscancel):
        def func(self):
            self.definecreateticket(num,ffzt,kcslinputtext,qyxq,
                                    xdsjtsinputtext,
                                    yxcbcdf,yhqmcinputtext,yhlx,
                                    yhms,gdjemzinputtext,sjjemzmiminputtext,sjjemzmimaxinputtext,
                                    zdxfinputtext,sypt,
                                    syfw,zdhyoptionxpath,zdshinputtext,isplsh,plfilepath,
                                    kfyqthddj,
                                    sfzctq,iscancel)
        return func

def __generateTestCases():
    from addticket.models import AddTicket

    addticket_all = AddTicket.objects.filter(testproject="营销系统").filter(testmodule="任务活动管理").filter(testpage="编辑代金券").order_by('id')
    rows_count = addticket_all.count()

    for addticket in addticket_all:

        if len(str(addticket.id)) == 1:
            addticketid = '0000%s'% addticket.id
        elif len(str(addticket.id)) == 2:
            addticketid = '000%s' % addticket.id
        elif len(str(addticket.id)) == 3:
            addticketid = '00%s' % addticket.id
        elif len(str(addticket.id)) == 4:
            addticketid = '0%s' % addticket.id
        elif len(str(addticket.id)) == 5:
            addticketid = '%s' % addticket.id
        else:
            addticketid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(addticket.id)
        args.append(addticket.ffzt)
        args.append(addticket.kcslinputtext)
        args.append(addticket.qyxq)
        args.append(addticket.xdsjtsinputtext)
        args.append(addticket.yxcbcdf)
        args.append("%s_%s"%(addticket.yhqmcinputtext,GetTimeStr().getTimeStr()))
        args.append(addticket.yhlx)
        args.append(addticket.yhms)
        args.append(addticket.gdjemzinputtext)
        args.append(addticket.sjjemzmiminputtext)
        args.append(addticket.sjjemzmimaxinputtext)
        args.append(addticket.zdxfinputtext)
        args.append(addticket.sypt)
        args.append(addticket.syfw)
        args.append(addticket.zdhyoptionxpath)
        args.append(addticket.zdshinputtext)
        args.append(addticket.isplsh)
        args.append(addticket.plfilepath)
        args.append(addticket.kfyqthddj)
        args.append(addticket.sfzctq)
        args.append(addticket.iscancel)

        setattr(TestEditTicketClass, 'test_func_%s_%s' % (addticketid,addticket.testcasetitle),
                TestEditTicketClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










