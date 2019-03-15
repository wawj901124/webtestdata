import time

from base.getcookie import GetCookie
from data.get_data_login_cookie import GetData

class GetCookieSleep:
    def __init__(self):
        self.file_name = "../dataconfig/getlogincookie.xls"
        self.sheet_id = 0
        self.data = GetData(self.file_name,self.sheet_id)   #实例化


    def getcookiesleep(self):
        while True:
            try:
                rows_count = self.data.get_case_lines()
                print("线程获取cookie启动")
                for i in range(1, rows_count):  # 循环，但去掉第一个
                    print("\n执行第%d行数据\n" % i)
                    outjsonfile = self.data.get_out_json_file_content(i)
                    outloginurl = self.data.get_out_login_url_content(i)
                    outloginaccountxpath = self.data.get_out_login_account_xpath_content(i)
                    outloginaccounttext = self.data.get_out_login_account_text_content(i)
                    outloginppasswordxpath = self.data.get_out_login_password_xpath_content(i)
                    outloginpasswordtext = self.data.get_out_login_password_text_content(i)
                    outloginbuttonxpath = self.data.get_out_login_button_xpath_content(i)

                    getcookiemanager = GetCookie(outjsonfile,outloginurl,outloginaccountxpath,outloginaccounttext,outloginppasswordxpath,outloginpasswordtext,outloginbuttonxpath) #实例化
                    getcookiemanager.writerCookieToJson()
                print("线程获取cookie结束")
                time.sleep(1200)
                print("等待1200秒")
            except Exception as e:
                print("出现异常,异常原因：%s" % e)
            finally:
                True


if __name__ == '__main__':
    starttime = time.time()
    print("开始时间：%s" % starttime)
    gcs = GetCookieSleep()
    gcs.getcookiesleep()



