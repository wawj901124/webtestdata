from webtestdata.settings import WEB_URL_TITLE

class MerchantListPage:
    pageurl = "%s/nereus/agent/v/#/merchant/list" % WEB_URL_TITLE
    keyword = ""
    keywordselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[1]/div/div/div[1]/div/span"
    keywordselectinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[2]/div/div/input"

    status = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/span"
    statusselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/div[3]/div[1]/div/span"

    searchbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/form/div/button"
    searchtableresult =  "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/table/tbody"
    searchtableresult2 = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[3]/table/tbody"


