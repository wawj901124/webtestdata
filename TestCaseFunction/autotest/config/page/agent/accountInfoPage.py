from webtestdata.settings import WEB_URL_TITLE

class AccountInfoPage:
    pageurl = "%s/nereus/agent/v/#/self/info" % WEB_URL_TITLE
    #---Basic info---#
    basicinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/span"
    basicinfotext = "Basic info"

    agentid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[1]/label"
    agentidtext = "Agent ID:"

    loginaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[2]/label"
    loginaccounttext = "Login account:"

    agentname = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[3]/label"
    agentnametext = "Agent name:"

    agenttype = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[4]/label"
    agenttypetext = "Agent type:"

    agentidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[1]/div/div"
    agentidvaluetext = "20004160"

    loginaccountvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[2]/div/div"
    loginaccountvaluetext = "6281122336666"

    agentnamevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[3]/div/div"
    agentnamevaluetext = "test"

    agenttypevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/form/div[4]/div/div"
    agenttypevaluetext = "BD"