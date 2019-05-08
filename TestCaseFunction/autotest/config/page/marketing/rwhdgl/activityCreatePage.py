from webtestdata.settings import WEB_URL_TITLE,AGENT_REVISE_MERCHANTID

class ActivityCreatePage:
    pageurl = "%s/nereus/manager/index#/merchant/list" % WEB_URL_TITLE

    yxhdcj = ""
    yxhdcj_text = u"营销活动创建"
    # ---基础信息---#
    jcxx  = ""
    jcxx_text = u"基础信息"

    hdmc = ""
    hdmc_text = u"活动名称"
    hdmc_input = ""

    hdsj = ""
    hdsj_text = u"活动时间"
    hdsj_starttime = ""
    hdsj_endtime = ""

    hdys = ""
    hdys_text = u"活动预算"
    hdys_input = ""

    tfqd = ""
    tfqd_text = u"投放渠道"
    tfqd_select = ""
    tfqd_select_nbqd_option = ""
    tfqd_select_wbqd_option = ""
    tfqd_select_nbqd_option_text = u"内部渠道"
    tfqd_select_wbqd_option_text = u"外部渠道"
    tfqd_fxk_app_checkbox = ""
    tfqd_fxk_web_checkbox = ""
    tfqd_fxk_sdk_checkbox = ""
    tfqd_fxk_app = ""
    tfqd_fxk_web = ""
    tfqd_fxk_sdk = ""
    tfqd_fxk_app_text = "APP"
    tfqd_fxk_web_text = "Web"
    tfqd_fxk_sdk_text = "SDK"

    hdbz = ""
    hdbz_text = ""
    hdbz_textarea = ""

    # ---活动任务规则---#
    hdrwgz = ""
    hdrwgz_text = u"活动任务规则"

    rwlx = ""
    rwlx_text = u"任务类型"
    rwlx_select = ""
    rwlx_select_zc_option = ""
    rwlx_select_jx_option = ""
    rwlx_select_zc_option_text = u"注册"
    rwlx_select_jx_option_text = u"交易"

    rwmb = ""
    rwmb_text = u"任务目标"
    rwmb_select = ""
    rwmb_select_wczc_option = ""
    rwmb_select_wcjx_option = ""
    rwmb_select_wczc_option_text = u"完成注册"
    rwmb_select_wcjx_option_text = u"完成交易"

    rwxz = ""
    rwxz_text = u"任务限制"

    tjxz = ""
    tjxz_text = u"添加限制"
    tjxz_select = ""
    rwmb_select_one_option = ""
    rwmb_select_two_option = ""
    rwmb_select_one_option_text = u""
    rwmb_select_two_option_text = u""

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
    jy_wcjy_jylx_checkbox = ""

    jy_wcjy_jylx_fxk_xf = ""
    jy_wcjy_jylx_fxk_xf_text = u"消费"
    jy_wcjy_jylx_fxk_xf_checkbox = ""
    jy_wcjy_jylx_fxk_cz = ""
    jy_wcjy_jylx_fxk_cz_text = u"充值"
    jy_wcjy_jylx_fxk_cz_checkbox = ""
    jy_wcjy_jylx_fxk_zz = ""
    jy_wcjy_jylx_fxk_zz_text = u"转账"
    jy_wcjy_jylx_fxk_zz_checkbox = ""

    # ---支付方式---#
    jy_wcjy_zffs = ""
    jy_wcjy_zffs_text = u"支付方式"
    jy_wcjy_zffs_checkbox = ""
    jy_wcjy_zffs_delete_icon = ""

    jy_wcjy_zffs_fxk_qbye = ""
    jy_wcjy_zffs_fxk_qbye_text = u"钱包余额"
    jy_wcjy_zffs_fxk_qbye_checkbox = ""

    jy_wcjy_zffs_fxk_yhk = ""
    jy_wcjy_zffs_fxk_yhk_text = u"银行卡"
    jy_wcjy_zffs_fxk_yhk_checkbox = ""

    # ---用户活动参与次数---#
    jy_wcjy_yhhdcycs = ""
    jy_wcjy_yhhdcycs_text = u"用户活动参与次数"
    jy_wcjy_yhhdcycs_delete_icon = ""

    jy_wcjy_yhhdcycs_mgyhzzcycs = ""
    jy_wcjy_yhhdcycs_mgyhzzcycs_text = u"每个用户最多参与次数"
    jy_wcjy_yhhdcycs_mgyhzzcycs_input = ""
    jy_wcjy_yhhdcycs_mgyhmrcycs = ""
    jy_wcjy_yhhdcycs_mgyhmrcycs_text = u"每个用户每日参与次数"
    jy_wcjy_yhhdcycs_mgyhmrcycs_input = ""

    # ---奖励信息---#
    jlxx = ""
    jlxx_text = u"奖励信息"

    jllx = ""
    jllx_text = u"奖励类型"
    jllx_select = ""
    jllx_select_gdjl_option = ""
    jllx_select_gdjl_option_text = u"固定奖励"

    # ---未添加奖励礼品时添加礼品---#
    w_jllp = ""
    w_jllp_text = u"奖励礼品"

    w_tjlp = ""
    w_tjlp_text = u"添加礼品"

    # ---已添加奖励礼品时添加礼品---#
    y_jllp = ""
    y_jllp_text = u"奖励礼品"

    y_jllp_table_xh = ""
    y_jllp_table_xh_text = u"序号"

    y_jllp_table_mc = ""
    y_jllp_table_mc_text = u"名称"

    y_jllp_table_ffzt = ""
    y_jllp_table_ffzt_text = u"发放状态"

    y_jllp_table_cz = ""
    y_jllp_table_cz_text = u"发放状态"

    y_tjlp = ""
    y_tjlp_text = u"添加礼品"

    cancelbutton = ""
    submitbutton = ""


















