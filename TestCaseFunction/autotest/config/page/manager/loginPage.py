from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE  #导入现网环境参数

class LoginPage:
    if ISONLINE:
        pageurl = "%s/nereus/manager/index#/login" % ONLINE_WEB_URL_TITLE
    else:
        pageurl = "%s/nereus/manager/index#/login" % TEST_WEB_URL_TITLE

    logintitle = "/html/body/div[1]/div[2]/form/div/p"          #登录框的title

    account = "/html/body/div[1]/div[2]/form/div/div[1]/input"  #登录框的账号输入框
    accounttip = "/html/body/div[1]/div[2]/form/div/em"   #登录框的账号输入框下方提示

    password = "/html/body/div[1]/div[2]/form/div/div[2]/input"   #登录框的密码输入框
    passwordtip = "/html/body/div[1]/div[2]/form/div/em[2]"   #登录框的密码输入框下方提示


    # vercode = "/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/div/div[1]/div[1]/div/input"   #登录框的验证码输入框
    # vercodetip = "/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[3]/div/div[2]"   #登录框的验证码输入框下方提示

    # logintip = "/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[4]/div/div"   #点击登录按钮后的提示

    loginbutton =  "/html/body/div[1]/div[2]/form/div/a[1]/span"   #登录按钮

    # forgetpassword = ""   #找回密码文字链接
    # code = "/html/body/div[1]/div[2]/form/div/div[2]/div[3]/img"   #图像验证码

    # loginbutton2 = "/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[5]/div/button"  # 出现验证码后，登录按钮的路径发生了变化