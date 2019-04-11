from webtestdata.settings import WEB_URL_TITLE,AGENT_CONTRAT_MERCHANID

class MerchantContratPage:
    pageurl = "%s/nereus/agent/v/#/merchant/contrat/%s" % (WEB_URL_TITLE,AGENT_CONTRAT_MERCHANID)

    #---Bank account---#
    bankaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/span"
    merchantnametext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/div/div"
    merchantidtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[2]/div/div"
    settlementswitch = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[3]/div/div/span"
    banktext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[4]/div/div"
    accountnametext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[5]/div/div"
    accountnumbertext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[6]/div/div"

    #---MPF-offine collect---#
    mpfoffinecollect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/span"
    minimumidrtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div"
    settlecycletext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div"
    refundsettingtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/div/div"
    mpfsettingstext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/div/div"
    mpfsettingsfixedtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[2]/table/tbody/tr/td[1]/div/div/span"
    mpfsettingfeepercenttext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/span"
    mpfsettingminimumfeeidr = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[2]/table/tbody/tr/td[3]/div/div/span"
