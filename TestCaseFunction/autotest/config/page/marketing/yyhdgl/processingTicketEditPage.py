from webtestdata.settings import WEB_URL_TITLE,AGENT_REVISE_MERCHANTID

class ProcessingTicketEditPage:
    pageurl = "%s/nereus/manager/index#/merchant/list" % WEB_URL_TITLE

    ################第一部分######################
    qid = ""
    qid_text = ""
    ffzt = ""
    ffzt_text = u"发放状态"
    ffzt_kq = ""
    ffzt_kq_text = u"开启"
    ffzt_kq_checkbox  =  "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/form/div[2]/div/div[2]/form/div[2]/div[2]/div/div/label[1]/span/input"

    ffzt_gb = ""
    ffzt_gb_text = u"关闭"
    ffzt_gb_checkbox  =  "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/form/div[2]/div/div[2]/form/div[2]/div[2]/div/div/label[2]/span/input"

    kcsl = ""
    kcsl_text = u"库存数量"
    kcsl_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/div[3]/form/div[2]/div[3]/div/div/input"
    kscl_input_down_text = ""
    kscl_input_down_text_text = u"不填写数量代表不限制发放数量"
    kcsl_zjkc_input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div[3]/div[2]/div/form/div[2]/div/div[2]/form/div[2]/div[4]/div/div/input"









