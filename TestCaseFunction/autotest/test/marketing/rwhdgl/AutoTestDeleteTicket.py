import unittest

from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE,TEST_MANAGER_LOGIN_ACCOUNT,TEST_MANAGER_LOGIN_PASSWORD   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE,ONLINE_MANAGER_LOGIN_ACCOUNT,ONLINE_MANAGER_LOGIN_PASSWORD  #导入现网环境参数


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
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityEditPage import ActivityEditPage  #导入未上线活动编辑页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.ticketCreatePage import TicketCreatePage   #导入创建优惠券页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityListPage import ActivityListPage   #导入活动列表页


class TestDeleteTicketClass(unittest.TestCase):  # 创建测试类

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
            self.activeweb.findElementByXpathAndInput(LoginPage().account,ONLINE_MANAGER_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,ONLINE_MANAGER_LOGIN_PASSWORD)
        else:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,TEST_MANAGER_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,TEST_MANAGER_LOGIN_PASSWORD)

        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = ActivityEditPage()
        self.testpageurl =self.testpage.pageurl   #测试页面url
        self.testpagehdmcinput = self.testpage.hdmc_input       # ---基础信息---#   活动名称输入框路劲
        self.testpagehdsjstarttime = self.testpage.hdsj_starttime # ---基础信息---#   活动时间开始时间输入框路径
        self.testpagehdsjendtime = self.testpage.hdsj_endtime  # ---基础信息---#   活动时间结束时间输入框路径
        self.testpagehdysinput  = self.testpage.hdys_input   # ---基础信息---#   活动预算输入框路径
        self.testpagetfqdselect = self.testpage.tfqd_select   # ---基础信息---#  投放渠道下拉框路径
        self.testpagehdbztextarea = self.testpage.hdbz_textarea   # ---基础信息---#  活动备注多行输入框路径
        self.testpagerwlxselect = self.testpage.rwlx_select       # ---活动任务规则---# 任务类型下拉框路径
        self.testpagejllxselect = self.testpage.jllx_select     # ---活动奖励---# 奖励类型下拉框路径
        self.testpagewtjlp = self.testpage.w_tjlp    # ---活动奖励---# 未添加礼品时，“添加礼品”文字链接路径

        self.testpagecancelbutton = self.testpage.cancelbutton   #取消按钮
        self.testpagesubmitbutton = self.testpage.submitbutton   #提交按钮

        ######################创建优惠券页面###############################
        self.ticketcreatepage = TicketCreatePage()   #创建优惠券页
        self.ticketcreatepage_kcsl_input  = self.ticketcreatepage.kcsl_input   #第一部分# 库存数量输入框路径
        self.ticketcreatepage_qyxq_select = self.ticketcreatepage.qyxq_select   #第一部分# 券有效期选择框路径
        self.ticketcreatepage_yhqsm_areatext  = self.ticketcreatepage.yhqsm_areatext    #第一部分# 优惠券说明多行输入框路径
        self.ticketcreatepage_yhqmc_input = self.ticketcreatepage.yhqmc_input    #第二部分# 优惠券名称输入框路径
        self.ticketcreatepage_yhlx_select = self.ticketcreatepage.yhlx_select    #第二部分# 优惠类型选择框路径
        self.ticketcreatepage_yhms_select = self.ticketcreatepage.yhms_select    #第二部分# 优惠模式选择框路径
        self.ticketcreatepage_zdxf_input = self.ticketcreatepage.zdxf_input    #第二部分# 最低消费输入框路径
        self.ticketcreatepage_zfqdxz_select  = self.ticketcreatepage.zfqdxz_select     #第二部分# 支付渠道限制选择框路径
        self.ticketcreatepage_syfw_select   = self.ticketcreatepage.syfw_select     #第二部分# 使用范围选择框路径

        self.ticketcreatepage_confirm_button = self.ticketcreatepage.confirm_button   #页面 确定按钮

        ######################活动列表页###############################
        self.activitylistpage = ActivityListPage()   #活动列表页
        self.activitylistpage_searchtableresult = self.activitylistpage.searchtableresult


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

    #定义创建活动,
    #投放渠道一级为1表示内部渠道，为2表示外部渠道
    #投放渠道二级为0表示全选，为1，2，等表示选一项和选多项组合，程序中只有全选和选择一项的情况
    # 任务类型为1表示注册，为2表示交易类型
    #奖励类型1表示固定奖励
    def definedeleteticket(self,num,
                             hdmcinputtext,hdysinputtext,
                             tfqdyj, tfqdej,hdbztextareainputtext,
                             rwlx,tjrwxz,
                             jyjylx, jyzffs,
                             jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
                             jllx,iscancel):
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #创建活动
        #填入基础信息部分
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdmcinput, hdmcinputtext)   #输入活动名称
        self.activeweb.findElementByXpathAndClickAbountData(num,self.testpagehdsjstarttime,self.testpage.hdsj_starttime_daytime,pathright=self.testpage.hdsj_starttime_rightmove,pathconfirm=self.testpage.hdsj_starttime_queding)   #点选活动时间开始时间
        self.activeweb.findElementByXpathAndClickAbountData(num,self.testpagehdsjendtime ,self.testpage.hdsj_endtime_daytime,pathright=self.testpage.hdsj_endtime_rightmove,pathconfirm=self.testpage.hdsj_endtime_queding)   #点选活动时间结束时间
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdysinput, hdysinputtext)   #输入活动预算
        if tfqdyj =="1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagetfqdselect,self.testpage.tfqd_select_nbqd_option)  # 投放渠道一级渠道选择内部渠道
            if ISONLINE:
                # 点击投放渠道二级渠道第一个选项
                if not self.activeweb.findElementByXpath(
                        self.testpage.tfqd_select_nbqd_fxk_mbmpay_checkbox).is_selected():
                    self.activeweb.findElementByXpathAndClickNum(num,
                                                                 self.testpage.tfqd_select_nbqd_fxk_mbmpay_checkbox)
                if self.activeweb.findElementByXpath(
                        self.testpage.tfqd_select_nbqd_fxk_mydisrupto_checkbox).is_selected():
                    self.activeweb.findElementByXpathAndClickNum(num,
                                                                 self.testpage.tfqd_select_nbqd_fxk_mydisrupto_checkbox)

                if self.activeweb.findElementByXpath(
                        self.testpage.tfqd_select_nbqd_fxk_qrindo_checkbox).is_selected():
                    self.activeweb.findElementByXpathAndClickNum(num,
                                                                 self.testpage.tfqd_select_nbqd_fxk_qrindo_checkbox)
            else:
                if tfqdej == "0":  # 点击投放渠道二级渠道所有项复选框
                    if not self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_mbmpay_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num,self.testpage.tfqd_select_nbqd_fxk_mbmpay_checkbox)
                    if not self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_mydisrupto_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_mydisrupto_checkbox)
                    if not self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_qrindo_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_qrindo_checkbox)
                    if not self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox)
                    if not self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_paysdk_checkbox)
                else:
                    if self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_mbmpay_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num,self.testpage.tfqd_select_nbqd_fxk_mbmpay_checkbox)
                    if self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_mydisrupto_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_mydisrupto_checkbox)
                    if self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_qrindo_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_qrindo_checkbox)
                    if self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox)
                    if self.activeweb.getEleImage(num,self.testpage.tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox).is_selected():
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_paysdk_checkbox)

                    if tfqdej == "1":
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_mbmpay_checkbox)   #点选投放渠道二级渠道mbmpay项复选框
                    elif tfqdej == "2":
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_mydisrupto_checkbox)   #点选投放渠道二级渠道mydisrupto项复选框
                    elif tfqdej == "3":
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_qrindo_checkbox)   #点选投放渠道二级渠道qrindo项复选框
                    elif tfqdej == "4":
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox)   #点选投放渠道二级渠道qrindomerchantcashier项复选框
                    elif tfqdej == "5":
                        self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_nbqd_fxk_paysdk_checkbox)   #点选投放渠道二级渠道paysdk项复选框

        # elif tfqdyj =="2":
        #     self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagetfqdselect,self.testpage.tfqd_select_wbqd_option)  # 投放渠道一级渠道选择外部渠道
        #     if tfqdej == '0':# 点击投放渠道二级渠道所有项复选框
        #         self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_app_checkbox)
        #         self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_web_checkbox)
        #         self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_sdk_checkbox)
        #     elif tfqdej == "1":
        #         self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_app_checkbox)   #点选投放渠道二级渠道app项复选框
        #     elif tfqdej == "2":
        #         self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_web_checkbox)   #点选投放渠道二级渠道web项复选框
        #     elif tfqdej == "3":
        #         self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tfqd_select_wbqd_fxk_web_checkbox)   #点选投放渠道二级渠道sdk项复选框

        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdbztextarea, hdbztextareainputtext)   #输入活动备注

        #填入活动任务规则部分
        if rwlx == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagerwlxselect,self.testpage.rwlx_select_zc_option)  # 任务类型选择注册
        elif rwlx=='2':
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagerwlxselect,self.testpage.rwlx_select_jx_option)  # 任务类型选择交易

            if jyjylx == "0":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_jylx_checkbox)  #点击交易类型全选框
            elif jyjylx == "1":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_jylx_fxk_xf_checkbox)  # 点击交易类型-消费前选择框
            elif jyjylx == "2":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_jylx_fxk_cz_checkbox)  # 点击交易类型-充值前选择框
            elif jyjylx == "3":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_jylx_fxk_zz_checkbox)  # 点击交易类型-转账前选择框

            #点击添加限制文字链接
            if tjrwxz == "1":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tjxz)  # 点击添加限制文字链接
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.rwmb_popup_jylx_option)  # 点击添加限制弹框中的交易类型
            elif tjrwxz == "2":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tjxz)  # 点击添加限制文字链接
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.rwmb_popup_zffs_option)  # 点击添加限制弹框中的支付方式
            elif tjrwxz == "3":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tjxz)  # 点击添加限制文字链接
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.rwmb_popup_yhhdcycs_option)  # 点击添加限制弹框中的用户活动参与次数
            elif tjrwxz == "4":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tjxz)  # 点击添加限制文字链接
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.rwmb_popup_zffs_option)  # 点击添加限制弹框中的支付方式
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.tjxz)  # 点击添加限制文字链接
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.rwmb_popup_yhhdcycs_option)  # 点击添加限制弹框中的用户活动参与次数



            if jyzffs == "0":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_zffs_checkbox)  #点击支付方式全选框
            elif jyzffs == "1":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_zffs_fxk_qbye_checkbox)  # 点击支付方式-钱包余额前选择框
            elif jyzffs == "2":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_zffs_fxk_yhk_checkbox)  # 点击支付方式-银行卡前选择框
            elif jyzffs == "3":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_zffs_fxk_yhkhq_checkbox)  # 点击支付方式-银行卡+券前选择框
            elif jyzffs == "4":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_zffs_fxk_yehq_checkbox)  # 点击支付方式-余额+券前选择框
            elif jyzffs == "5":
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.jy_wcjy_zffs_fxk_vahspg_checkbox)  # 点击支付方式-VA或SPG支付前选择框

            print("jymgyhzdcycsinputtext:%s" % jymgyhzdcycsinputtext)
            if jymgyhzdcycsinputtext != None:
                self.activeweb.findElementByXpathAndInputNum(num, self.testpage.jy_wcjy_yhhdcycs_mgyhzdcycs_input, jymgyhzdcycsinputtext)  # 输入每个用户最多参与次数
            if jymgyhmrcycsinputtext != None:
                self.activeweb.findElementByXpathAndInputNum(num, self.testpage.jy_wcjy_yhhdcycs_mgyhmrcycs_input, jymgyhmrcycsinputtext)  # 输入每个用户每日参与次数

        #填入活动奖励部分
        if jllx =="1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagejllxselect,self.testpage.jllx_select_gdjl_option)  # 选择奖励类型为固定奖励

        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpage.y_jllp_table_cz_just_two_first_delete)  # 点击奖励礼品中的第一条数据中"删除"
        # self.activeweb.delayTime(5000)
        self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpage.delete_popup_confirm)   #点击删除弹框中的确认按钮


        if iscancel:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagecancelbutton)  # 点击取消按钮
        else:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagesubmitbutton)  # 点击提交按钮
            # 断言活动列表中是否有新增加的活动
            self.defineisintable(num, self.activitylistpage_searchtableresult, hdmcinputtext, 1)





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
                self.activeweb.outPutMyLog("在【%s】中存在:【%s】"% (value[int(tablecolnum)],expecttext))
                notexsitflag = False
                break
        if notexsitflag:
            self.activeweb.outPutMyLog("在【%s】不存在：【%s】"% (tabledic,expecttext))
            self.assertTrue(False)



    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,hdmcinputtext,hdysinputtext,
                    tfqdyj, tfqdej,hdbztextareainputtext,
                    rwlx,tjrwxz,
                    jyjylx, jyzffs,
                    jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
                    jllx,iscancel):
        def func(self):
            self.definedeleteticket(num,
                             hdmcinputtext,hdysinputtext,
                             tfqdyj, tfqdej,hdbztextareainputtext,
                             rwlx,tjrwxz,
                             jyjylx, jyzffs,
                             jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
                             jllx,iscancel)
        return func

def __generateTestCases():
    from addactivity.models import AddActivity

    addactivity_all = AddActivity.objects.filter(testproject="营销系统").filter(testmodule="任务活动管理").filter(testpage="创建活动").filter(id=19).order_by('id')
    rows_count = addactivity_all.count()

    for addactivity in addactivity_all:

        if len(str(addactivity.id)) == 1:
            addactivityid = '0000%s'% addactivity.id
        elif len(str(addactivity.id)) == 2:
            addactivityid = '000%s' % addactivity.id
        elif len(str(addactivity.id)) == 3:
            addactivityid = '00%s' % addactivity.id
        elif len(str(addactivity.id)) == 4:
            addactivityid = '0%s' % addactivity.id
        elif len(str(addactivity.id)) == 5:
            addactivityid = '%s' % addactivity.id
        else:
            addactivityid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(addactivity.id)
        args.append("%s_%s"%(addactivity.hdmcinputtext,GetTimeStr().getTimeStr()))
        args.append(addactivity.hdysinputtext)
        args.append(addactivity.tfqdyj)
        args.append(addactivity.tfqdej)
        args.append(addactivity.hdbztextareainputtext)
        args.append(addactivity.rwlx)
        args.append(addactivity.tjrwxz)
        args.append(addactivity.jyjylx)
        args.append(addactivity.jyzffs)
        args.append(addactivity.jymgyhzdcycsinputtext)
        args.append(addactivity.jymgyhmrcycsinputtext)
        args.append(addactivity.jllx)
        args.append(addactivity.iscancel)

        setattr(TestDeleteTicketClass, 'test_func_%s_%s' % (addactivityid,addactivity.testcasetitle),
                TestDeleteTicketClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










