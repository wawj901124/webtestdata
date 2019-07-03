from webtestdata.settings import WEB_URL_TITLE

class AddMerchantSuccessPage:
    # pageurl = "%s/nereus/agent/v/#/merchant/add" % WEB_URL_TITLE
    success = "/html/body/div[4]/div[2]/div/div/div/div/div[2]/div"
    successtext = "Success"
    okbutton = "/html/body/div[4]/div[2]/div/div/div/div/div[3]/button"
    successindividu = "/html/body/div[4]/div[2]/div/div/div/div/div[1]/div"
    okbuttonindividu = "/html/body/div[4]/div[2]/div/div/div/div/div[2]/button"