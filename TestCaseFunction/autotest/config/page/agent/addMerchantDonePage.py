from webtestdata.settings import WEB_URL_TITLE

class AddMerchantDonePage:
    # pageurl = "%s/nereus/agent/v/#/merchant/add" % WEB_URL_TITLE
    done = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/p[2]"
    donetext = "Done"
    waitingforapproval = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/p[3]/span"
    waitingforapprovaltext = "Waiting For Review"
    merchantnamevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/p[4]/span[2]"
    merchantnamevaluetext = "test_company"
    merchantlistbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div/div/button"