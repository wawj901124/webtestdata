from webtestdata.settings import WEB_URL_TITLE,MARKETING_DETAIL_ACTIVITYID

class ActivityDetialsPage:
    pageurl = "%s/nereus/marketing/admin/v/#/activityManage/missionAct/missionDetail/%s" % (WEB_URL_TITLE,MARKETING_DETAIL_ACTIVITYID)

    yxhdcj = ""
    yxhdcj_text = u"营销活动创建"
    # ---基础信息---#
    jcxx  = ""
    jcxx_text = u"基础信息"

    hdid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/div/span"


    hdmc = ""
    hdmc_text = u"活动名称"
    hdmc_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[1]/div/div/input"


    hdlx = ""
    hdlx_text = u"活动类型"
    hdlx_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/span"

    hdlx_select_lx_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[3]/div/div/div[2]/ul[2]/li[1]"
    hdlx_select_ch_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[3]/div/div/div[2]/ul[2]/li[2]"
    hdlx_select_lc_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[3]/div/div/div[2]/ul[2]/li[3]"
    hdlx_select_zh_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[3]/div/div/div[2]/ul[2]/li[4]"
    hdlx_select_tsbc_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[3]/div/div/div[2]/ul[2]/li[5]"
    hdlx_select_lx_option_text = u"拉新"
    hdlx_select_ch_option_text = u"促活"
    hdlx_select_lc_option_text = u"留存"
    hdlx_select_zh_option_text = u"转化"
    hdlx_select_tsbc_option_text = u"投诉补偿"


    hdsj = ""
    hdsj_text = u"活动时间"
    hdsj_starttime =  "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/input"
    hdsj_starttime_rightmove = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div[1]/div[2]/div/div/div/div[1]/span[5]/i"
    hdsj_starttime_daytime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div[1]/div[2]/div/div/div/div[2]/div/span[22]/em"
    hdsj_starttime_secondtime = ""
    hdsj_starttime_queding = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[4]/div/div[1]/div[2]/div/div/div/div[4]/button[3]"
    hdsj_endtime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div[1]/div/input"
    hdsj_endtime_rightmove = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div[2]/div/div/div/div[1]/span[5]/i"
    hdsj_endtime_daytime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div[2]/div/div/div/div[2]/div/span[24]/em"
    hdsj_endtime_secondtime = ""
    hdsj_endtime_queding = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div[2]/div/div/div/div[4]/button[3]"

    hdys = ""
    hdys_text = u"活动预算"
    hdys_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[6]/div/div/input"


    hdbz = ""
    hdbz_text = u"活动备注"
    hdbz_textarea = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[7]/div/div/textarea"


    # ---活动奖励---#
    jlxx = ""
    jlxx_text = u"奖励信息"

    jllx = ""
    jllx_text = u"奖励类型"
    jllx_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/span"

    jllx_select_gdjl_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/ul[2]/li"
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

    y_jllp_table_cz = ""
    y_jllp_table_cz_text = u"操作"

    y_jllp_table_cz_just_one_edit = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[5]/div/div/a[2]"
    y_jllp_table_cz_just_one_detail = ""
    y_jllp_table_cz_just_two_first_delete = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[5]/div/div/a[3]"
    delete_popup_confirm = "/html/body/div[5]/div/div/div/span[1]"



    y_tjlp = ""
    y_tjlp_text = u"添加礼品"


    cancelbutton ="/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/span[1]"
    submitbutton ="/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/span[2]"


















