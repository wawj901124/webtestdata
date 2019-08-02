
class LoginWithPasswordPage(object):
    account_input_resourceId = "com.ahdi.qrindo.wallet:id/et_login_phone_number"
    passwoord_input_resourceId = "com.ahdi.qrindo.wallet:id/et_login_pwd"
    login_btn_text = "Login"
    forgotpassword_text = "Forgot password?"
    loginwithotp_text = "Log in with OTP"
    signup_text = "Sign up"

loginwithpasswordpage = LoginWithPasswordPage()


class LoginWithPasswordPageCommonFunction(object):

    #定义登录函数
    def define_login_function(self,baseframe,accountinputtext,passswordinputtext):
        #账号输入框中输入内容
        baseframe.findelement_and_input("resourceId",loginwithpasswordpage.account_input_resourceId,accountinputtext)
        #密码输入框中输入内容
        baseframe.findelement_and_input("resourceId",loginwithpasswordpage.passwoord_input_resourceId,passswordinputtext)
        #点击登录
        baseframe.findelement_and_click("text",loginwithpasswordpage.login_btn_text)

loginwithpasswordpage_commonfunction = LoginWithPasswordPageCommonFunction()

