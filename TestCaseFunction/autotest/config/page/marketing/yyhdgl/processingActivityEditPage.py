from webtestdata.settings import WEB_URL_TITLE,MARKETING_EDIT_PROCESSING_ACTIVITYID

from TestCaseFunction.util.gettimestr import GetTimeStr

class ProcesingActivityEditPage:
    filename = "createactivityid.txt"
    editactivityid = GetTimeStr().readText(filename)
    pageurl = "%s/nereus/marketing/admin/v/#/activityManage/missionAct/modifyOnLine/%s" % (WEB_URL_TITLE,editactivityid )
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



















