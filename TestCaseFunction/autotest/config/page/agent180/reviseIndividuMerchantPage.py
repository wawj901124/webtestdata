from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE  #导入现网环境参数

from TestCaseFunction.util.gettimestr import GetTimeStr


class ReviseIndividuMerchantPage:
    filename = "merchantid.txt"
    revisemerchantid = GetTimeStr().readText(filename)
    if ISONLINE:
        pageurl = "%s/nereus/agent/v/#/merchant/revice/%s" % (ONLINE_WEB_URL_TITLE,revisemerchantid)
    else:
        pageurl = "%s/nereus/agent/v/#/merchant/revice/%s" % (TEST_WEB_URL_TITLE, revisemerchantid)

    auditnotapprovedtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div/p[2]"
    submitagainbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[1]/div/button"

    # ---Merchant info---#
    merchantinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[1]/span"
    brandnameinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[1]/div/div/input"
    brandnametip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[1]/div/div[2]"
    emailinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[2]/div/div/input"
    emailtip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[2]/div/div[2]"
    contactnumberinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[3]/div/div/input"
    contactnumbertip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[3]/div/div[2]"
    merchanttypeselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/span"
    merchanttypetip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[4]/div/div[2]"
    merchanttypeselectindividu = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[4]/div/div/div[2]/ul[2]/li[1]"
    merchanttypeselectcompany = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[4]/div/div/div[2]/ul[2]/li[2]"
    categoryselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[5]/div/div/div[1]/div/span"
    categorytip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[5]/div/div[2]"
    criteriaselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/span"
    criteriatip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[6]/div/div[2]"
    siupinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[7]/div/div[1]/input"
    siuptip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[7]/div/div[2]"
    provinceselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[8]/div/div/div[1]/div/span"
    provincetip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[8]/div/div[2]"
    cityselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[9]/div/div/div[1]/div/span"
    citytip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[9]/div/div[2]"
    districtinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[10]/div/div[1]/input"
    districttip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[10]/div/div[2]"
    villageinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[11]/div/div[1]/input"
    villagetip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[11]/div/div[2]"
    postcodeinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[12]/div/div/input"
    postcodetip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[12]/div/div[2]"
    addressinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[13]/div/div[1]/input"
    addresstip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[13]/div/div[2]"
    photosiupimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[14]/div/div/div/div/div"

    photonpwpcompanyimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[15]/div/div/div/div/div"
    phototdpimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div[16]/div/div/div/div/div"

    # ---Owner / Person in Charge info---#
    ownerpersoninchangeinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[1]/span"
    nameinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[1]/div/div/input"
    nametip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[1]/div/div[2]"
    npwpinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input"
    npwptip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[2]/div/div[2]"
    typeidselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[3]/div/div/div[1]/div/span"
    typeidtip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[3]/div/div[2]"
    identitynumberinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[4]/div/div/input"
    identitynumbertip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[4]/div/div[2]"
    address2input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[5]/div/div/input"
    address2tip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[5]/div/div[2]"
    nationalityselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[6]/div/div/div[1]/div/span"
    nationalitytip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[6]/div/div[2]"
    phoneinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[7]/div/div/input"
    phonetip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[7]/div/div[2]"
    email2input = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[8]/div/div/input"
    email2tip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[8]/div/div[2]"
    photofullfacebustimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[9]/div/div/div/div/div"
    photofullfacebusttip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[9]/div/div[2]"

    # ---Profile Photos---#
    profilephotos = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[3]/div[1]/span"
    locationphotoimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[3]/div[2]/div/div[1]/div/div/div/div/div"
    locationphototip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[3]/div[2]/div/div[1]/div/div[2]"
    photoofthecashiersdeskimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[3]/div[2]/div/div[2]/div/div/div/div/div"
    otherphotoimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[3]/div[2]/div/div[3]/div/div/div/div/div"

    # ---Bank account---#
    bankaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[1]/span"
    bankselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[1]/div/div/div[1]/div/span"
    banktip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[1]/div/div[2]"
    accountnameinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/input"
    accountnametip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[2]/div/div[2]"
    accountnumberinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[3]/div/div[1]/input"
    accountnumbertip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[3]/div/div[2]"

    # ---QRindo account---#
    qrindoaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[1]/span"
    qrindoaccountinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[2]/div/div/div/div/input"
    qrindoaccounttip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[2]/div/div/div/div[2]"
    checkbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[2]/div/div/div/div/div[2]/button"