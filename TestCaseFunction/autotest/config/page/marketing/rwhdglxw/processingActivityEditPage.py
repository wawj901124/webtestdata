from webtestdata.settings import WEB_URL_TITLE,MARKETING_EDIT_PROCESSING_ACTIVITYID

from TestCaseFunction.util.gettimestr import GetTimeStr

class ProcesingActivityEditPage:
    filename = "createactivityid.txt"
    editactivityid = GetTimeStr().readText(filename)
    pageurl = "%s/nereus/marketing/admin/v/#/activityManage/missionAct/modifyOffLine/%s" % (WEB_URL_TITLE,editactivityid )
    # pageurl = "%s/nereus/marketing/admin/v/#/activityManage/missionAct/modifyOffLine/%s" % (WEB_URL_TITLE, MARKETING_EDIT_PROCESSING_ACTIVITYID)
    yxhdcj = ""
    yxhdcj_text = u"营销活动创建"
    # ---基础信息---#
    jcxx  = ""
    jcxx_text = u"基础信息"

    hdmc = ""
    hdmc_text = u"活动名称"
    hdmc_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[2]/div/div/input"

    hdsj = ""
    hdsj_text = u"活动时间"
    hdsj_starttime = ""
    hdsj_starttime_rightmove = ""
    hdsj_starttime_daytime = ""
    hdsj_starttime_secondtime = ""
    hdsj_starttime_queding = ""
    hdsj_endtime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div[1]/div/input"
    hdsj_endtime_rightmove = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/div/div[1]/span[5]/i"
    hdsj_endtime_daytime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/div/div[2]/div/span[26]/em"
    hdsj_endtime_secondtime = ""
    hdsj_endtime_queding = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div[2]/div/div/div/div[4]/button[3]"

    hdys = ""
    hdys_text = u"活动预算"
    hdys_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/input"

    hdys_zjys_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[6]/div/div/input"

    tfqd = ""
    tfqd_text = u"投放渠道"
    tfqd_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/span"
    tfqd_select_nbqd_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[6]/div/div/div[2]/ul[2]/li"
    tfqd_select_wbqd_option = ""
    tfqd_select_nbqd_option_text = u"内部渠道"
    tfqd_select_wbqd_option_text = u"外部渠道"
    tfqd_select_nbqd_fxk_mbmpay_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[7]/div/div/label[1]/span/input"
    tfqd_select_nbqd_fxk_mydisrupto_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[7]/div/div/label[2]/span/input"
    tfqd_select_nbqd_fxk_qrindo_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[7]/div/div/label[3]/span/input"
    tfqd_select_nbqd_fxk_qrindomerchantcashier_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[7]/div/div/label[4]/span/input"
    tfqd_select_nbqd_fxk_paysdk_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[7]/div/div/label[5]/span/input"

    tfqd_select_nbqd_fxk_app = ""
    tfqd_select_nbqd_fxk_web = ""
    tfqd_select_nbqd_fxk_sdk = ""
    tfqd_select_nbqd_fxk_app_text = "APP"
    tfqd_select_nbqd_fxk_web_text = "Web"
    tfqd_select_nbqd_fxk_sdk_text = "SDK"
    tfqd_select_wbqd_fxk_app_checkbox = ""
    tfqd_select_wbqd_fxk_web_checkbox = ""
    tfqd_select_wbqd_fxk_sdk_checkbox = ""
    tfqd_select_wbqd_fxk_app = ""
    tfqd_select_wbqd_fxk_web = ""
    tfqd_select_wbqd_fxk_sdk = ""
    tfqd_select_wbqd_fxk_app_text = "APP"
    tfqd_select_wbqd_fxk_web_text = "Web"
    tfqd_select_wbqd_fxk_sdk_text = "SDK"

    hdbz = ""
    hdbz_text = ""
    hdbz_textarea = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[8]/div/div/textarea"

    # ---活动任务规则---#
    hdrwgz = ""
    hdrwgz_text = u"活动任务规则"

    rwlx = ""
    rwlx_text = u"任务类型"
    rwlx_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/span"
    rwlx_select_zc_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[1]"
    rwlx_select_jx_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/ul[2]/li[2]"
    rwlx_select_zc_option_text = u"注册"
    rwlx_select_jx_option_text = u"交易"

    rwmb = ""
    rwmb_text = u"任务目标"
    rwmb_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/span"
    rwmb_select_wczc_option = ""
    rwmb_select_wcjx_option = ""
    rwmb_select_wczc_option_text = u"完成注册"
    rwmb_select_wcjx_option_text = u"完成交易"

    rwxz = ""
    rwxz_text = u"任务限制"

    tjxz = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[1]/div/div[1]/button"
    tjxz_text = u"添加限制"
    # ---添加限制弹框中选项---#
    rwmb_popup_jylx_option = ""
    rwmb_popup_zffs_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[1]/div/div[2]/ul/li[1]"
    rwmb_popup_yhhdcycs_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[1]/div/div[2]/ul/li[2]"
    rwmb_popup_jylx_option_text = u"交易类型"
    rwmb_popup_zffs_option_text = u"支付方式"
    rwmb_popup_yhhdcycs_option_text = u"用户活动参与次数"


    # ---注册-完成注册-任务限制---#
    zc_zcwc_yh = ""
    zc_zcwc_yh_text = u"用户"
    zc_zcwc_yh_checkbox = ""

    zc_zcwc_yh_fxk_xzcyh = ""
    zc_zcwc_yh_fxk_xzcyh_text = u"新注册用户"
    zc_zcwc_yh_fxk_xzcyh_checkbox = ""
    zc_zcwc_yh_fxk_xbkyh = ""
    zc_zcwc_yh_fxk_xbkyh_text = u"新绑卡用户"
    zc_zcwc_yh_fxk_xbkyh_checkbox = ""
    zc_zcwc_yh_fxk_wzfgyh = ""
    zc_zcwc_yh_fxk_wzfgyh_text = u"未支付过用户"
    zc_zcwc_yh_fxk_wzfgyh_checkbox = ""

    zc_zcwc_yhhdcycs = ""
    zc_zcwc_yhhdcycs_text = u"用户活动参与次数"
    zc_zcwc_yhhdcycs_delete_icon = ""

    zc_zcwc_yhhdcycs_mgyhzzcycs = ""
    zc_zcwc_yhhdcycs_mgyhzzcycs_text = u"每个用户最多参与次数"
    zc_zcwc_yhhdcycs_mgyhzzcycs_input = ""
    zc_zcwc_yhhdcycs_mgyhmrcycs = ""
    zc_zcwc_yhhdcycs_mgyhmrcycs_text = u"每个用户每日参与次数"
    zc_zcwc_yhhdcycs_mgyhmrcycs_input = ""

    # ---交易-完成交易-任务限制---#
    # ---交易类型---#
    jy_wcjy_jylx = ""
    jy_wcjy_jylx_text = u"交易类型"
    jy_wcjy_jylx_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div/span/label/label/span/input"

    jy_wcjy_jylx_fxk_xf = ""
    jy_wcjy_jylx_fxk_xf_text = u"消费"
    jy_wcjy_jylx_fxk_xf_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/label[1]/span/input"
    jy_wcjy_jylx_fxk_cz = ""
    jy_wcjy_jylx_fxk_cz_text = u"充值"
    jy_wcjy_jylx_fxk_cz_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/label[2]/span/input"
    jy_wcjy_jylx_fxk_zz = ""
    jy_wcjy_jylx_fxk_zz_text = u"转账"
    jy_wcjy_jylx_fxk_zz_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/label[3]/span/input"

    # ---支付方式---#
    jy_wcjy_zffs = ""
    jy_wcjy_zffs_text = u"支付方式"
    jy_wcjy_zffs_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[3]/span/label/label/span/input"
    jy_wcjy_zffs_delete_icon = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[3]/span/i"

    jy_wcjy_zffs_fxk_qbye = ""
    jy_wcjy_zffs_fxk_qbye_text = u"钱包余额"
    jy_wcjy_zffs_fxk_qbye_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[3]/div/div/label[2]/span/input"

    jy_wcjy_zffs_fxk_yhkhq_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[3]/div/div/label[3]/span/input"
    jy_wcjy_zffs_fxk_yehq_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[3]/div/div/label[4]/span/input"
    jy_wcjy_zffs_fxk_vahspg_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[3]/div/div/label[5]/span/input"
    jy_wcjy_zffs_fxk_yhk = ""
    jy_wcjy_zffs_fxk_yhk_text = u"银行卡"
    jy_wcjy_zffs_fxk_yhk_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[3]/div/div/label[1]/span/input"

    # ---用户活动参与次数---#
    jy_wcjy_yhhdcycs = ""
    jy_wcjy_yhhdcycs_text = u"用户活动参与次数"
    jy_wcjy_yhhdcycs_delete_icon = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[4]/span[1]/i"

    jy_wcjy_yhhdcycs_mgyhzdcycs = ""
    jy_wcjy_yhhdcycs_mgyhzdcycs_text = u"每个用户最多参与次数"
    jy_wcjy_yhhdcycs_mgyhzdcycs_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[4]/span[2]/div[1]/div/div/input"
    jy_wcjy_yhhdcycs_mgyhmrcycs = ""
    jy_wcjy_yhhdcycs_mgyhmrcycs_text = u"每个用户每日参与次数"
    jy_wcjy_yhhdcycs_mgyhmrcycs_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div/div[4]/span[2]/div[2]/div/div/input"

    # ---活动奖励---#
    jlxx = ""
    jlxx_text = u"活动奖励"

    jllx = ""
    jllx_text = u"奖励类型"
    jllx_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/div[1]/div/div/div[1]/div/span"
    jllx_select_gdjl_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/div[1]/div/div/div[2]/ul[2]/li"
    jllx_select_gdjl_option_text = u"固定奖励"

    # ---未添加奖励礼品时添加礼品---#
    w_jllp = ""
    w_jllp_text = u"奖励礼品"

    w_tjlp = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/div[2]/div/button"
    w_tjlp_text = u"添加礼品"

    # ---已添加奖励礼品时添加礼品---#
    y_jllp = ""
    y_jllp_text = u"奖励礼品"
    y_jllp_table = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody"


    y_jllp_table_xh = ""
    y_jllp_table_xh_text = u"序号"

    y_jllp_table_mc = ""
    y_jllp_table_mc_text = u"名称"

    y_jllp_table_ffzt = ""
    y_jllp_table_ffzt_text = u"发放状态"

    y_jllp_table_ffzt_result_just_one = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/form/div[2]/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/span"

    y_jllp_table_cz = ""
    y_jllp_table_cz_text = u"操作"

    y_jllp_table_cz_just_one_edit = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/form/div[2]/div/div/div/div[2]/table/tbody/tr/td[5]/div/div/a[2]"
    y_jllp_table_cz_just_one_detail = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/form/div[2]/div/div/div/div[2]/table/tbody/tr/td[5]/div/div/a[1]"


    y_tjlp = ""
    y_tjlp_text = u"添加礼品"


    cancelbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/span[1]"
    submitbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/span[2]"


















