
from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE  #导入现网环境参数

from TestCaseFunction.util.gettimestr import GetTimeStr

class MerchantContractPage:
    filename = "merchantid.txt"
    checkcontractmerchantid = GetTimeStr().readText(filename)
    if ISONLINE:
        pageurl = "%s/nereus/agent/v/#/merchant/contrat/%s" % (ONLINE_WEB_URL_TITLE,checkcontractmerchantid)
    else:
        pageurl = "%s/nereus/agent/v/#/merchant/contrat/%s" % (TEST_WEB_URL_TITLE, checkcontractmerchantid)

    #---Bank account---#
    bankaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/span"
    bankaccounttext = "Bank account"

    merchantname = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/label"
    merchantnametext = "Merchant name："
    merchantid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[2]/label"
    merchantidtext = "Merchant ID:"

    settlement = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[3]/label"
    settlementtext = "Settlement："

    bank = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[4]/label"
    banktext = "Bank："

    accountname = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[5]/label"
    accountnametext = "Account name："

    accountnumber = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[6]/label"
    accountnumbertext = "Account number："

    merchantnamevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/div/div"
    merchantnamevaluetext = "test_individu_20190415152327"

    merchantidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[2]/div/div"
    merchantidvaluetext = AGENT_CONTRAT_MERCHANID

    settlementswitch = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[3]/div/div/span"

    bankvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[4]/div/div"
    bankvaluetext = "BRI"

    accountnamevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[5]/div/div"
    accountnamevaluetext = "test_individu"

    accountnumbervalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[6]/div/div"
    accountnumbervaluetext = "test_individu"

    #---MPF-offine collect---#
    mpfoffinecollect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/span"
    mpfoffinecollecttext = "MPF-offine collect"

    minimumidr = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/label"
    minimumidrtext = "Minimum(IDR)："

    settlecycle = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[2]/label"
    settlecycletext = "Settlement cycle："

    refundsetting = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/label"
    refundsettingtext = "Refund setting："

    mpfsettings = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/label"
    mpfsettingstext = "MPF setting："

    mpfladder = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/label"
    mpfladdertext = "MPF ladder："

    mpfladderfixed = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[1]/table/thead/tr/th[1]/div/span"
    mpfladderfixedtext = "Fixed"

    mpfladderfeepercent = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[1]/table/thead/tr/th[2]/div/span"
    mpfladderfeepercenttext = "Fee（%）"

    mpfladdefeeminimum = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[1]/table/thead/tr/th[3]/div/span"
    mpfladdefeeminimumtext = "Fee minimum"

    minimumidrvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div"
    minimumidrvaluetext = "20,000"

    settlecyclevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div"
    settlecyclevaluetext = "T+1"

    refundsettingvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/div/div"
    refundsettingvaluetext = "All fees return"

    mpfsettingsvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/div/div"
    mpfsettingsvaluetext = "base on transaction amount"

    mpfladderfixedvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[2]/table/tbody/tr/td[1]/div/div/span"
    mpfladderfixedvaluetext = "0"

    mpfladderfeepercentvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/span"
    mpfladderfeepercentvaluetext = "0"

    mpfladdefeeminimumvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div[2]/table/tbody/tr/td[3]/div/div/span"
    mpfladdefeeminimumvaluetext = "0"