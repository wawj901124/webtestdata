from webtestdata.settings import WEB_URL_TITLE,AGENT_DETAILS_MERCHANTID,AGENT_LOGIN_ACCOUNT

class CompanyDetailsPage:
    pageurl = "%s/nereus/agent/v/#/merchant/detail/%s" % (WEB_URL_TITLE,AGENT_DETAILS_MERCHANTID)

    #---Basic info---#
    basicinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/span"
    basicinfotext = "Basic info"
    # ---key---#
    merchantid  = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/label"
    merchantidtext = "Merchant ID:"
    loginaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[2]/label"
    loginaccounttext = "Login account:"
    agent = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[3]/label"
    agenttext = "Agent:"
    brandname = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/label"
    brandnametext = "Brand name:"
    # ---value---#
    merchantidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/div/div"
    merchantidvaluetext = AGENT_DETAILS_MERCHANTID
    loginaccountvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[2]/div/div"
    loginaccountvaluetext = "62%s"% AGENT_LOGIN_ACCOUNT
    agentvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[3]//div/div"
    agentvaluetext = "test"
    brandnamevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div"
    brandnamevaluetext = "test_individu_20190415152327"

    #---Merchant info---#
    merchantinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/span"
    merchantinfotext = "Merchant info"
    # ---key---#
    # email = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[2]/label"
    # emailtext = "Email:"
    # contactnumber = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/label"
    # contactnumbertext = "Contact number:"
    merchanttype = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/label"
    merchanttypetext = "Merchant type:"
    category = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/label"
    categorytext = "Category:"
    criteria = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[6]/label"
    criteriatext = "Criteria:"
    # siup = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[7]/label"
    # siuptext = "SIUP:"
    province = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[8]/label"
    provincetext = "Province:"
    city = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[9]/label"
    citytext = "City:"
    district = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[10]/label"
    districttext = "District:"
    village = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[11]/label"
    villagetext = "Village:"
    postcode = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[12]/label"
    postcodetext = "Postcode:"
    address = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[13]/label"
    addresstext = "Address:"
    companyname = ""      #公司专有
    companynametext = "Company name:"   #公司专有
    officialwebsite = ""   #公司专有
    officialwebsitetext = "Official website:"   #公司专有
    npwptaxid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[16]/label"   #公司专有
    npwptaxidtext = "NPWP / TAX ID:"   #公司专有
    photonpwpcompany = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[15]/label"
    photonpwpcompanytext = "Photo NPWP Company:"
    phototdp = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[16]/label"
    phototdptext = "Photo TDP:"

    # ---value---#
    merchanttypevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/div/div"
    merchanttypevaluetext = "Individu"
    categoryvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div"
    categoryvaluetext = "PASSENGER TRANSPORTATION"
    criteriavalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[6]/div/div"
    criteriavaluetext = "Micro"
    provincevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[8]/div/div"
    provincevaluetext = "JAWA BARAT"
    cityvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[9]/div/div"
    cityvaluetext = "Jawa Barat"
    districtvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[10]/div/div"
    districtvaluetext = "test_individu"
    villagevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[11]/div/div"
    villagevaluetext = "test_individu"
    postcodevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[12]/div/div"
    postcodevaluetext = "test_individu"
    addressvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[13]/div/div"
    addressvaluetext = "test_individu"
    companynamevalue = ""   #公司专有
    officialwebsitevalue = ""   #公司专有
    npwptaxidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[16]/div/div"   #公司专有
    photonpwpcompanyimagevalue = ""
    phototdpimagevalue = ""

    #---Owner / Person in Charge info---#
    ownerpersoninchangeinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[1]/span"
    ownerpersoninchangeinfotext = "Owner / Person in Charge info"
    # ---key---#
    name = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[1]/label"
    nametext = "Name:"
    # npwp = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[2]/label"  #个人专有
    # npwptext = "NPWP:"   #个人专有
    # typeid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[3]/label"   #个人专有
    # typeidtext = "Type ID:"   #个人专有
    # identitynumber = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[4]/label"   #个人专有
    # identitynumbertext = "Identity number:"   #个人专有
    # address2 = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[5]/label"   #个人专有
    # address2text = "Address:"   #个人专有
    # nationality = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[6]/label"   #个人专有
    # nationalitytext = "Nationality:"   #个人专有
    phone = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[7]/label"
    phonetext = "Phone:"
    email2 = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[8]/label"
    email2text = "Email:"
    position = ""   #公司专有
    positiontext = ""   #公司专有
    photofullfacebust = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[9]/label"
    photofullfacebusttext = "Photo PIC Full-faceBust:"
    # ---value---#
    namevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[1]/div/div"
    namevaluetext = "test_20190411"
    # npwpvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[2]/div/div"   #个人专有
    # npwpvaluetext = "test_individu"   #个人专有
    # typeidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[3]/div/div"   #个人专有
    # typeidvaluetext = "KTP"   #个人专有
    # identitynumbervalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[4]/div/div"   #个人专有
    # identitynumbervaluetext = "test_individu"   #个人专有
    # address2value = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[5]/div/div"   #个人专有
    # address2valuetext = "test_individu"   #个人专有
    # nationalityvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[6]/div/div"   #个人专有
    # nationalityvaluetext = "Indonesian"   #个人专有
    phonevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[7]/div/div"
    phonevaluetext = "test_individu"
    email2value= "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[8]/div/div"
    email2valuetext = "xiangkaizheng@iapppay.com"
    positionvalue = ""   #公司专有
    positionvaluetext = ""   #公司专有
    photofullfacebustimage ="/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[9]/div/div/div/div/div[1]/figure/a/img"

    #---Profile Photos---#
    profilephotos = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[1]/span"
    profilephotostext = "Profile Photos"
    # ---key---#
    locationphoto = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[1]/label"
    locationphototext = "Location Photo:"
    photoofthecashiersdesk = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[2]/label"
    photoofthecashiersdesktext = "Photo of the cashiers desk:"
    otherphoto = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[3]/label"
    otherphototext = "Other Photo:"




