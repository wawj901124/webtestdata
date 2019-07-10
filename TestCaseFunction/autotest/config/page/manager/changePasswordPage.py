from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE  #导入现网环境参数

class ChangePasswordPage:
    if ISONLINE:
        pageurl = "%s/nereus/manager/index#/account/changePwd" % ONLINE_WEB_URL_TITLE
    else:
        pageurl = "%s/nereus/manager/index#/account/changePwd" % TEST_WEB_URL_TITLE

    currentpassword = ""          #旧密码
    currentpasswordinput = "/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[1]/div[1]/p/span[2]/input"
    currentpasswordinputtip = "/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[1]/div[1]/p/em"

    newpassword = ""          #新密码
    newpasswordinput = "/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[1]/div[2]/p/span[2]/input"
    newpasswordinputtip = "/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[1]/div[2]/p/em"

    confirmpassword = ""          #确认密码
    confirmpasswordinput = "/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[1]/div[3]/p/span[2]/input"
    confirmpasswordinputtip = "/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[1]/div[3]/p/em"

    submitbutton = "/html/body/div[3]/div[2]/ui-view/div[2]/div/form/div[2]/button"

