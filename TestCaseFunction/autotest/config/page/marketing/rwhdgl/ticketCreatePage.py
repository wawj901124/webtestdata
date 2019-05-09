from webtestdata.settings import WEB_URL_TITLE,AGENT_REVISE_MERCHANTID

class TicketCreatePage:
    pageurl = "%s/nereus/manager/index#/merchant/list" % WEB_URL_TITLE

    ################第一部分######################
    ffzt = ""
    ffzt_text = u"发放状态"
    ffzt_kq = ""
    ffzt_kq_text = u"开启"
    ffzt_kq_checkbox  = ""
    ffzt_gb = ""
    ffzt_gb_text = u"关闭"
    ffzt_gb_checkbox  = ""

    kcsl = ""
    kcsl_text = u"库存数量"
    kcsl_input = ""
    kscl_input_down_text = ""
    kscl_input_down_text_text = u"不填写数量代表不限制发放数量"

    qyxq = ""
    qyxq_text = u"券有效期"
    qyxq_select = ""
    qyxq_select_option_xdsj = ""
    qyxq_select_option_xdsj_ts_input = ""
    qyxq_select_option_xdsj_t = ""
    qyxq_select_option_xdsj_t_text = u"天"
    qyxq_select_option_xdsj_down_text = ""
    qyxq_select_option_xdsj_down_text_text = u"相对时间例：设置30天,成功发券后优惠券30天内有效。"

    qyxq_select_option_jdsj = ""
    qyxq_select_option_jdsj_starttime = ""
    qyxq_select_option_jdsj_endtime = ""
    qyxq_select_option_jdsj_down_text = ""
    qyxq_select_option_jdsj_down_text_text = u"绝对时间，通过时间段筛选控件选择固定时段内有效"

    yxcbcdf = ""
    yxcbcdf_text = u"营销成本承担方"
    yxcbcdf_pt = ""
    yxcbcdf_pt_text = u"平台"
    yxcbcdf_pt_checkbox = ""
    yxcbcdf_sh = ""
    yxcbcdf_sh_text = u"平台"
    yxcbcdf_sh_checkbox = ""

    yhqsm = ""
    yhqsm_text = u"优惠券说明"
    yhqsm_areatext = ""

    ################第二部分######################
    yhqmc = ""
    yhqmc_text = u"优惠券名称"
    yhqmc_input = ""

    yhlx = ""
    yhlx_text = u"优惠类型"
    yhlx_select = ""
    yhlx_option_djq = ""

    yhms = ""
    yhms_text = u"优惠模式"
    yhms_select = ""
    yhms_select_option_gdje = ""
    yhms_select_option_gdje_mz = ""
    yhms_select_option_gdje_mz_text = u"面值"
    yhms_select_option_gdje_mz_input = ""
    yhms_select_option_gdje_mz_lb = ""
    yhms_select_option_gdje_mz_lb_text = u"卢比"
    yhms_select_option_sjje = ""
    yhms_select_option_sjje_mz = ""
    yhms_select_option_sjje_mz_text = u"面值"
    yhms_select_option_sjje_mz_min = ""
    yhms_select_option_sjje_mz_min_text = "MIN"
    yhms_select_option_sjje_mz_min_input = ""
    yhms_select_option_sjje_mz_min_lb = ""
    yhms_select_option_sjje_mz_min_lb_text = u"卢比"
    yhms_select_option_sjje_mz_max = ""
    yhms_select_option_sjje_mz_max_text = "MAX"
    yhms_select_option_sjje_mz_max_input = ""
    yhms_select_option_sjje_mz_max_lb = ""
    yhms_select_option_sjje_mz_max_lb_text = u"卢比"

    zdxf = ""
    zdxf_text = u"最低消费"
    zdxf_input = ""

    zfqdxz = ""
    zfqdxz_text = u"支付渠道限制"
    zfqdxz_select = ""
    zfqdxz_select_option_bx = ""
    zfqdxz_select_option_qbye = ""
    zfqdxz_select_option_yhkzf = ""

    sypt = ""
    sypt_text = u"使用平台"
    sypt_QRindo = ""
    sypt_QRindo_text = u"QRindo"
    sypt_QRindo_checkbox = ""
    sypt_PaySDK = ""
    sypt_PaySDK_text = u"PaySDK"
    sypt_PaySDK_checkbox = ""

    syfw = ""
    syfw_text = u"使用范围"
    syfw_select = ""
    syfw_select_option_bx = ""
    syfw_select_option_zdhy = ""
    syfw_select_option_zdhy_select = ""
    syfw_select_option_zdhy_select_option = ""
    syfw_select_option_zdhy_tjhy_button = ""
    syfw_select_option_zdhy_tjhy = ""

    syfw_select_option_zdsh = ""
    syfw_select_option_zdsh_input = ""
    syfw_select_option_zdsh_tjsh_button = ""
    syfw_select_option_zdsh_tjsh_table = ""
    syfw_select_option_zdsh_tjsh_table_detele = ""
    syfw_select_option_zdsh_pltjsh_button = ""
    syfw_select_option_zdsh_pltjsh_plwj = ""
    syfw_select_option_zdsh_pltjsh_plwj_text = u"批量文件"
    syfw_select_option_zdsh_pltjsh_file = ""
    syfw_select_option_zdsh_pltjsh_file_delete = ""
    syfw_select_option_zdsh_pltjsh_areatext = ""

    kfyqthddj = ""
    kfyqthddj_text = u"可否与其他活动叠加"
    kfyqthddj_bkdjsy = ""
    kfyqthddj_bkdjsy_text = u"不可叠加使用"
    kfyqthddj_bkdjsy_checkbox = ""
    kfyqthddj_kydjsy = ""
    kfyqthddj_kydjsy_text = u"可以叠加使用"
    kfyqthddj_kydjsy_checkbox = ""

    sfzctq = ""
    sfzctq_text = u"是否支持退券"
    sfzctq_kt = ""
    sfzctq_kt_text = u"可退"
    sfzctq_kt_checkbox = ""
    sfzctq_bkt = ""
    sfzctq_bkt_text = u"不可退"
    sfzctq_bkt_checkbox = ""

    cancel_button = ""
    confirm_button = ""












