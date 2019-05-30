from webtestdata.settings import WEB_URL_TITLE

class MerchantListPage:
    pageurl = "%s/nereus/manager/index#/merchant/list" % WEB_URL_TITLE

    searchbutton = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[1]/form/div[3]/p/span/a/span"
    searchtableresult = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[2]/table/tbody[1]"
    searchtableresult2 = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[2]/table/tbody[1]"

    keywordselectxpath = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[1]/form/div[1]/select"
    keywordoption_merchantname_xpath = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[1]/form/div[1]/select/option[1]"
    keywordoption_merchantid_xpath = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[1]/form/div[1]/select/option[2]"
    keywordoption_merchantid_text = "Merchant id"
    keywordselectinputxpath = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[1]/form/div[1]/input"
    firstdatareview = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[2]/table/tbody[1]/tr/td[7]/a[2]"

    statusselectxpath = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[1]/form/div[2]/select"
    reviewtextlinkxpath = "/html/body/div[3]/div[2]/ui-view/ui-view/div[2]/div[1]/div[1]/div[2]/table/tbody[1]/tr[1]/td[7]/a[2]"









