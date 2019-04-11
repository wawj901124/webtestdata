from webtestdata.settings import WEB_URL_TITLE,AGENT_DETAILS_MERCHANTID

class DetailsPage:
    pageurl = "%s/nereus/agent/v/#/merchant/detail/%s" % (WEB_URL_TITLE,AGENT_DETAILS_MERCHANTID)

    #---Merchant info---#
    merchantinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/span"
    brandnametext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div"

    emailtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div"

    contactnumbertext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/div/div"

    merchanttypetext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/div/div"

    categorytext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div"

    criteriatext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[6]/div/div"

    siuptext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[7]/div/div"

    provincetext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[8]/div/div"

    citytext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[9]/div/div"

    districttext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[10]/div/div"

    villagetext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[11]/div/div"

    postcodetext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[12]/div/div"

    addresstext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[13]/div/div"

    companynametext = ""
    officialwebsitetext = ""
    npwptaxidtext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[16]/div/div"

    photosiupimage = ""
    photonpwpcompanyimage = ""
    phototdpimage = ""

    #---Owner / Person in Charge info---#
    ownerpersoninchangeinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[1]/span"
    nametext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[1]/div/div"
    npwptext = ""
    typeidselect = ""
    identitynumberinput = ""
    address2input = ""
    nationalityselect = ""
    phonetext = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[3]/div/div"
    email2text = ""
    photofullfacebustimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[5]/div/div/div/div/div[1]/figure/a/img"

    #---Profile Photos---#
    profilephotos = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[1]/span"
    locationphotoimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[1]/div/div/div/div/div[1]/figure/a/img"

    photoofthecashiersdeskimage = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[2]/div/div/div/div/div[1]/figure/a/img"
    otherphotoimage = ""

    #---Bank account---#
    bankaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[1]/span"
    bankselect = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[1]/div/div/div[1]/div/span"
    banktip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[1]/div/div[2]"
    accountnameinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/input"
    accountnametip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[2]/div/div[2]"
    accountnumberinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[3]/div/div[1]/input"
    accountnumbertip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[3]/div/div[2]"

    #---QRindo account---#
    qrindoaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[1]/span"
    qrindoaccountinput = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[2]/div/div/div/div/input"
    qrindoaccounttip = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[2]/div/div/div/div[2]"
    checkbutton = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/form/div[2]/div[5]/div[2]/div/div/div/div/div[2]/button"




