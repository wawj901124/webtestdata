from webtestdata.settings import WEB_URL_TITLE

class AccountInfoPage:
    pageurl = "%s/nereus/agent/v/#/self/info" % WEB_URL_TITLE
    #---Basic info---#
    basicinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/span"
    agentidtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[1]/div/div"
    loginaccounttext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[2]/div/div"
    agentnametext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[3]/div/div"
    agenttypetext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[4]/div/div"
