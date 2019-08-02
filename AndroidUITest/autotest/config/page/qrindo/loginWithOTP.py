
class LoginWithOtpPage(object):
    login_btn_text = "Login"
    loginwithpassword_text = "Log in with Password"
    account_input_resourceId = "com.ahdi.qrindo.wallet:id/et_login_phone_number_otp"
    signup_text = "Sign up"

loginwithotppage = LoginWithOtpPage()


class LoginWithOtpPageCommonFunction(object):

    def define_click_loginwithpassword_function(self,baseframe):
        #点击Login in with pawword
        baseframe.findelement_and_click("text",loginwithotppage.loginwithpassword_text)

    def define_is_loginwithpassword_exist_function(self,baseframe):
        is_exist = baseframe.ele_is_exist("text", loginwithotppage.loginwithpassword_text)
        return is_exist


loginwithotppage_commonfunction  = LoginWithOtpPageCommonFunction()