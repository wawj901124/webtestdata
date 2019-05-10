from webtestdata.settings import WEB_URL_TITLE,AGENT_REVISE_MERCHANTID

class ActivityListPage:
    pageurl = "%s/nereus/manager/index#/merchant/list" % WEB_URL_TITLE

    searchtableresult = ""

    hdlb = ""
    hdlb_text = u"活动列表"
    # ---筛选字段---#
    sx_hdmc = ""
    sx_hdmc_text = u"活动名称"
    sx_hdmc_input = ""

    sx_cjsj = ""
    sx_cjsj_text = u"创建时间"
    sx_cjsj_starttime = ""
    sx_cjsj_endtime = ""

    sx_hdzt = ""
    sx_hdzt_text = u"活动状态"
    sx_hdzt_select = ""
    sx_hdzt_select_qb_option = ""
    sx_hdzt_select_dsx_option = ""
    sx_hdzt_select_jxz_option = ""
    sx_hdzt_select_yjs_option = ""
    sx_hdzt_select_qb_option_text = u"全部"
    sx_hdzt_select_dsx_option_text = u"待上线"
    sx_hdzt_select_jxz_option_text = u"进行中"
    sx_hdzt_select_yjs_option_text = u"已结束"

    sx_rwlx = ""
    sx_rwlx_text = u"任务类型"
    sx_rwlx_select = ""
    sx_rwlx_select_qb_option = ""
    sx_rwlx_select_zchd_option = ""
    sx_rwlx_select_wszlhd_option = ""
    sx_rwlx_select_lxhd_option = ""
    sx_rwlx_select_qb_option_text = u"全部"
    sx_rwlx_select_zchd_option_text = u"注册活动"
    sx_rwlx_select_wszlhd_option_text = u"完善资料活动"
    sx_rwlx_select_lxhd_option_text = u"拉新活动"

    cx_button = ""

    xjhd_button = ""

    # ---表格表头字段---#
    bg_xh = ""
    bg_xh_text = u"序号"
    bg_hd = ""
    bg_hd_text = u"活动"
    bg_hdsj = ""
    bg_hdsj_text = u"活动时间"
    bg_tfqd = ""
    bg_tfqd_text = u"投放渠道"
    bg_rwlx = ""
    bg_rwlx_text = u"任务类型"
    bg_hdlx = ""
    bg_hdlx_text = u"活动状态"
    bg_cjsj = ""
    bg_cjsj_text = u"创建时间"
    bg_cjr = ""
    bg_cjr_text = u"创建人"
    bg_cz = ""
    bg_cz_text = u"操作"

    content_sx = ""
    content_sx_text = u"上线"
    content_xx = ""
    content_xx_text = u"下线"
    content_xq = ""
    content_xq_text = u"详情"
    content_bj = ""
    content_bj_text = u"编辑"

