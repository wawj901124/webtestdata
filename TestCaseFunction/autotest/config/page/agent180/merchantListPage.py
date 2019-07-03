from webtestdata.settings import WEB_URL_TITLE

class MerchantListPage:
    pageurl = "%s/nereus/agent/v/#/merchant/list" % WEB_URL_TITLE

    searchbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/button"
    searchtableresult = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/table/tbody"
    searchtableresult2 = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[3]/table/tbody"

    keywordselectxpath = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[1]/div/div/div[1]/div/span"
    keywordoption_merchantname_xpath = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[1]/div/div/div[2]/ul[2]/li[1]"
    keywordselectinputxpath = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[2]/div/div/input"

    statusselectxpath = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[3]/div[1]/div/span"


    #-----------筛选字段-----------#
    keyword = ""
    keywordtext = "Keyword"

    keyword_merchantname = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[1]/div/div/div[2]/ul[2]/li[1]"
    keyword_merchantname_text = "Merchant name"
    keyword_merchantid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[1]/div/div/div[2]/ul[2]/li[2]"
    keyword_merchantid_text = "Merchant id"
    keyword_loginaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[1]/div/div/div[2]/ul[2]/li[3]"
    keyword_loginaccount_text = "Login account"

    status_shaixuan = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/span"
    status_shaixuan_text = "Status"
    status_all = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[3]/div[2]/ul[2]/li[1]"
    status_all_text = "All"
    status_waitingforreview = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[3]/div[2]/ul[2]/li[2]"
    status_waitingforreview_text = "Waiting For Review"
    status_unapproved = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[3]/div[2]/ul[2]/li[3]"
    status_unapproved_text = "Unapproved"
    status_normal = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[3]/div[2]/ul[2]/li[4]"
    status_normal_text = "Normal"
    status_disabled = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[3]/div[2]/ul[2]/li[5]"
    status_disabled_text = "Disabled"

    #-----------表格title内容-----------#
    merchantnameid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[2]/div/span"
    merchantnameidtext = "Merchant name（ID）"

    loginaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[3]/div/span"
    loginaccounttext = "Login account"

    category = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[4]/div/span"
    categorytext = "Category"

    registrationtime = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[5]/div/span"
    registrationtimetext = "Registration time"

    status = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[6]/div/span"
    statustext = "Status"

    operation = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[7]/div/span"
    operationtext = "Operation"

    operation_waitingforreview_details = ""










