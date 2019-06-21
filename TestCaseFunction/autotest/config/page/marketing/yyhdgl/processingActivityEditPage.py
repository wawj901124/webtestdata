
from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE  #导入现网环境参数

from TestCaseFunction.util.gettimestr import GetTimeStr

class ProcesingActivityEditPage:
    filename = "createactivityid.txt"
    editactivityid = GetTimeStr().readText(filename)
    if ISONLINE:
        pageurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s" % (ONLINE_WEB_URL_TITLE,editactivityid )
    else:
        pageurl = "%s/nereus/marketing/admin/v/#/activityManage/operation/modifyOffLine/%s" % (TEST_WEB_URL_TITLE, editactivityid)
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
    hdsj_endtime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div/div/div[1]/div/input"

    hdsj_endtime_rightmove = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div/div/div[2]/div/div/div/div[1]/span[5]/i"

    hdsj_endtime_daytime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div/div/div[2]/div/div/div/div[2]/div/span[26]/em"
    hdsj_endtime_secondtime = ""
    hdsj_endtime_queding = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[5]/div/div/div/div/div[2]/div/div/div/div[4]/button[3]"

    hdys = ""
    hdys_text = u"活动预算"

    hdys_zjys = ""
    hdys_zjys_text = "增加预算"
    hdys_zjys_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div[2]/div/div[7]/div/div/input"


    # ---已添加奖励礼品时添加礼品---#
    y_jllp = ""
    y_jllp_text = u"奖励礼品"
    y_jllp_table = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody"


    y_jllp_table_xh = ""
    y_jllp_table_xh_text = u"序号"

    y_jllp_table_mc = ""
    y_jllp_table_mc_text = u"名称"

    y_jllp_table_ffzt = ""
    y_jllp_table_ffzt_text = u"发放状态"

    y_jllp_table_ffzt_result_just_one = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/form/div[2]/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/span"



    y_jllp_table_cz = ""
    y_jllp_table_cz_text = u"操作"

    y_jllp_table_cz_just_one_edit = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/form/div[2]/div/div/div/div[2]/table/tbody/tr/td[5]/div/div/a[2]"


    y_jllp_table_cz_just_one_detail = ""
    y_jllp_table_cz_just_two_first_delete = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[5]/div/div/a[3]"
    delete_popup_confirm = "/html/body/div[5]/div/div/div/span[1]"



    y_tjlp = ""
    y_tjlp_text = u"添加礼品"




    cancelbutton ="/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/span[1]"
    submitbutton ="/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/span[2]"
















