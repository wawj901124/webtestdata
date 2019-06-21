
class TicketEditPage:

    ################第一部分######################
    qid = ""
    qid_text = ""
    ffzt = ""
    ffzt_text = u"发放状态"
    ffzt_kq = ""
    ffzt_kq_text = u"开启"
    ffzt_kq_checkbox  = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[2]/div/div/label[1]/span/input"

    ffzt_gb = ""
    ffzt_gb_text = u"关闭"
    ffzt_gb_checkbox  = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[2]/div/div/label[2]/span/input"

    kcsl = ""
    kcsl_text = u"库存数量"
    kcsl_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[3]/div/div/input"
    kscl_input_down_text = ""
    kscl_input_down_text_text = u"不填写数量代表不限制发放数量"

    qyxq = ""
    qyxq_text = u"券有效期"
    qyxq_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[1]/div/div/div[1]/div/span"
    qyxq_select_option_xdsj = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[1]/div/div/div[2]/ul[2]/li[2]"
    qyxq_select_option_xdsj_ts_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[2]/div/div[1]/input"
    qyxq_select_option_xdsj_t = ""
    qyxq_select_option_xdsj_t_text = u"天"
    qyxq_select_option_xdsj_down_text = ""
    qyxq_select_option_xdsj_down_text_text = u"相对时间例：设置30天,成功发券后优惠券30天内有效。"

    qyxq_select_option_jdsj = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[1]/div/div/div[2]/ul[2]/li[1]"
    qyxq_select_option_jdsj_starttime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[2]/div/div[1]/div/div/div[1]/div/input"
    qyxq_select_option_jdsj_starttime_pathright = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[1]/span[5]/i"
    qyxq_select_option_jdsj_starttime_daytime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/span[22]/em"

    qyxq_select_option_jdsj_endtime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[2]/div/div[2]/div/div/div[1]/div/input"
    qyxq_select_option_jdsj_endtime_pathright = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/span[5]/i"
    qyxq_select_option_jdsj_endtime_daytime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[4]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/span[24]/em"
    qyxq_select_option_jdsj_down_text = ""
    qyxq_select_option_jdsj_down_text_text = u"绝对时间，通过时间段筛选控件选择固定时段内有效"

    yxcbcdf = ""
    yxcbcdf_text = u"营销成本承担方"
    yxcbcdf_pt = ""
    yxcbcdf_pt_text = u"平台"
    yxcbcdf_pt_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[5]/div/div/label[1]/span/input"
    yxcbcdf_sh = ""
    yxcbcdf_sh_text = u"商户"
    yxcbcdf_sh_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[5]/div/div/label[2]/span/input"

    yhqsm = ""
    yhqsm_text = u"优惠券说明"
    yhqsm_areatext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[6]/div/div/textarea"

    ################第二部分######################
    yhqmc = ""
    yhqmc_text = u"优惠券名称"
    yhqmc_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[7]/div/div/input"

    yhlx = ""
    yhlx_text = u"优惠类型"
    yhlx_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[8]/div/div/div[1]/div/span"
    yhlx_option_djq = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[8]/div/div/div[2]/ul[2]/li"

    yhms = ""
    yhms_text = u"优惠模式"
    yhms_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[9]/div/div/div[1]/div/span"
    yhms_select_option_gdje = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[9]/div/div/div[2]/ul[2]/li[1]"
    yhms_select_option_gdje_mz = ""
    yhms_select_option_gdje_mz_text = u"面值"
    yhms_select_option_gdje_mz_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[10]/div/div/input"
    yhms_select_option_gdje_mz_lb = ""
    yhms_select_option_gdje_mz_lb_text = u"卢比"
    yhms_select_option_sjje = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[9]/div/div/div[2]/ul[2]/li[2]"
    yhms_select_option_sjje_mz = ""
    yhms_select_option_sjje_mz_text = u"面值"
    yhms_select_option_sjje_mz_min = ""
    yhms_select_option_sjje_mz_min_text = "MIN"
    yhms_select_option_sjje_mz_min_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[10]/div/div[1]/div/div/input"
    yhms_select_option_sjje_mz_min_lb = ""
    yhms_select_option_sjje_mz_min_lb_text = u"卢比"
    yhms_select_option_sjje_mz_max = ""
    yhms_select_option_sjje_mz_max_text = "MAX"
    yhms_select_option_sjje_mz_max_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[10]/div/div[2]/div/div/input"
    yhms_select_option_sjje_mz_max_lb = ""
    yhms_select_option_sjje_mz_max_lb_text = u"卢比"

    zdxf = ""
    zdxf_text = u"最低消费"
    zdxf_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[11]/div/div/input"

    zfqdxz = ""
    zfqdxz_text = u"支付渠道限制"
    zfqdxz_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[12]/div/div/div[1]/div/span"
    zfqdxz_select_option_bx = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[12]/div/div/div[2]/ul[2]/li"
    zfqdxz_select_option_qbye = ""
    zfqdxz_select_option_yhkzf = ""

    sypt = ""
    sypt_text = u"使用平台"
    sypt_QRindo = ""
    sypt_QRindo_text = u"QRindo"
    sypt_mbmpay_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[13]/div/div/label[1]/span/input"
    sypt_mydisrupto_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[13]/div/div/label[2]/span/input"
    sypt_QRindo_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[13]/div/div/label[3]/span/input"
    sypt_qrindomerchantcashier_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[13]/div/div/label[4]/span/input"

    sypt_PaySDK = ""
    sypt_PaySDK_text = u"PaySDK"
    sypt_PaySDK_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[13]/div/div/label[5]/span/input"

    syfw = ""
    syfw_text = u"使用范围"
    syfw_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[14]/div/div/div[1]/div/span"
    syfw_select_option_bx = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[14]/div/div/div[2]/ul[2]/li[1]"
    syfw_select_option_zdhy = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[14]/div/div/div[2]/ul[2]/li[2]"
    syfw_select_option_zdhy_select = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div/div[1]/div/span"
    syfw_select_option_zdhy_select_option_one = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div/div[2]/ul[2]/li[1]"
    syfw_select_option_zdhy_tjhy_button = ""
    syfw_select_option_zdhy_tjhy = ""

    syfw_select_option_zdsh = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[14]/div/div/div[2]/ul[2]/li[3]"
    syfw_select_option_zdsh_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[1]/div/div[1]/div/input"
    syfw_select_option_zdsh_input_option_one = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[1]/div/div[2]/ul[2]/li"
    syfw_select_option_zdsh_tjsh_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[1]/button"
    syfw_select_option_zdsh_tjsh_table = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[3]/div/div/div[2]/table/tbody"
    syfw_select_option_zdsh_tjsh_table_detele_one = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[3]/div/div/div[2]/table/tbody/tr/td[4]/div/div/a"
    syfw_select_option_zdsh_qbsc_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[3]/button"
    syfw_select_option_zdsh_qbsc_qd_button = "/html/body/div[5]/div/div/div/span[1]"
    syfw_select_option_zdsh_qbsc_qx_button = "/html/body/div[5]/div/div/div/span[2]"
    syfw_select_option_zdsh_pltjsh_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[2]/div/button"
    syfw_select_option_zdsh_pltjsh_plwj = ""
    syfw_select_option_zdsh_pltjsh_plwj_text = u"批量文件"
    syfw_select_option_zdsh_pltjsh_file = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[2]/ul/li/span"
    syfw_select_option_zdsh_pltjsh_file_delete = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[2]/ul/li/i"
    syfw_select_option_zdsh_pltjsh_areatext_div = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div[3]"

    kfyqthddj = ""
    kfyqthddj_text = u"可否与其他活动叠加"
    kfyqthddj_bkdjsy = ""
    kfyqthddj_bkdjsy_text = u"不可叠加使用"
    kfyqthddj_bkdjsy_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div/label[1]/span/input"
    kfyqthddj_kydjsy = ""
    kfyqthddj_kydjsy_text = u"可以叠加使用"
    kfyqthddj_kydjsy_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[15]/div/div/label[2]/span/input"

    sfzctq = ""
    sfzctq_text = u"是否支持退券"
    sfzctq_kt = ""
    sfzctq_kt_text = u"可退"
    sfzctq_kt_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[16]/div/div/label[1]/span/input"
    sfzctq_bkt = ""
    sfzctq_bkt_text = u"不可退"
    sfzctq_bkt_checkbox = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[16]/div/div/label[2]/span/input"

    cancel_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[17]/span[1]"
    confirm_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[17]/span[2]"

    cancel_button_zdsh = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[18]/span[1]"
    confirm_button_zdsh = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/form/div[2]/div[18]/span[2]"












