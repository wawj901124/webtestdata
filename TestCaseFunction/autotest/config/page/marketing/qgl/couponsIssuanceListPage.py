from webtestdata.settings import WEB_URL_TITLE

class CouponsIssuanceListPage:
    pageurl = "%s/nereus/marketing/admin/v/#/voucher/voucherList" % WEB_URL_TITLE

    searchtableresult = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/table/tbody"
    searchtableresult2 = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[3]/table/tbody"

    # ---筛选字段---#
    sx_hdmc = ""
    sx_hdmc_text = u"活动名称"
    sx_hdmc_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/input"
    sx_hdmc_input_list_one = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/ul[2]/li[1]"

    sx_hjyh = ""
    sx_hjyh_text = "获奖用户"
    sx_hjyh_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div[1]/div/input"
    sx_hjyh_input_list_one = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div[2]/ul[2]/li"



    sx_ffzt = ""
    sx_ffzt_text = u"发放状态"
    sx_ffzt_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[3]/div/div[1]/div/span"
    sx_ffzt_select_qb_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[3]/div/div[2]/ul[2]/li[1]"
    sx_ffzt_select_clz_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[3]/div/div[2]/ul[2]/li[2]"
    sx_ffzt_select_sb_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[3]/div/div[2]/ul[2]/li[3]"
    sx_ffzt_select_cg_option = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[3]/div/div[2]/ul[2]/li[4]"
    sx_ffzt_select_qb_option_text = u"全部"
    sx_ffzt_select_clz_option_text = u"处理中"
    sx_ffzt_select_sb_option_text = u"失败"
    sx_ffzt_select_cg_option_text = u"成功"


    sx_cjsj = ""
    sx_cjsj_text = u"创建时间"
    sx_cjsj_starttime = ""
    sx_cjsj_endtime = ""

    sx_lsh = ""
    sx_lsh_text = "流水号"
    sx_lsh_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[5]/div/input"

    cx_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/button"


    # ---表格表头字段---#
    bg_xh = ""
    bg_xh_text = u"序号"
    bg_lsh = ""
    bg_lsh_text = u"流水号"
    bg_sshd = ""
    bg_sshd_text = u"所属活动"
    bg_hjyh = ""
    bg_hjyh_text = u"获奖用户"
    bg_jllp = ""
    bg_jllp_text = u"奖励礼品"
    bg_qqqd = ""
    bg_qqqd_text = u"请求渠道"
    bg_cjsj = ""
    bg_cjsj_text = u"创建时间"
    bg_ffzt = ""
    bg_ffzt_text = u"发放状态"
    bg_wcsj = ""
    bg_wcsj_text = u"完成时间"

    last_page = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/ul/li[6]/a"
