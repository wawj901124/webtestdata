#独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","webtestdata.settings")

import django
django.setup()

from inputtip.models import InputTipData

from db_tools.importinputtipdata.importexceldata.dataconfig.get_exceldata import GetData


#对数据遍历入库
class ReadData:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name==None:
            self.filename = '../data/exceldata/商户平台v1.5.1.xls'
        else:
            self.filename = file_name

        if sheet_id ==None:
            self.sheetid = 0
        else:
            self.sheetid = sheet_id
        self.exceldata = GetData(file_name=self.filename,sheet_id=self.sheetid)

    def readData(self):
        rows_count = self.exceldata.get_case_lines()   #获取表的行数
        for i in range(1,rows_count):   #循环遍历表数据
            inputtipdata = InputTipData()    #数据库的对象等于InputTipData,实例化
            inputtipdata.testproject = self.exceldata.get_testproject(i)   #填写测试项目
            inputtipdata.testmodule = self.exceldata.get_testmodule(i)  # 填写测试模块
            inputtipdata.testpage = self.exceldata.get_testpage(i)    #填写测试页面
            inputtipdata.testcasetitle = self.exceldata.get_testcasetitle(i)  # 填写测试内容的名称
            inputtipdata.isinput = self.exceldata.get_isinput(i)   #填写是否输入内容
            inputtipdata.inputxpath = self.exceldata.get_inputxpath(i)   #填写输入框Xpath路径
            inputtipdata.inputtext = self.exceldata.get_inputtext(i)   #填写输入框的输入内容
            inputtipdata.inputtipxpath = self.exceldata.get_inputtipxpath(i)   #填写输入框下Tip提示信息Xpath路径
            inputtipdata.inputtiptext = self.exceldata.get_inputtiptext(i)   #填写输入框下Tip提示信息内容
            inputtipdata.save()  #保存到数据库


if __name__ == "__main__":
    readdata = ReadData(file_name=r"D:\Users\Administrator\PycharmProjects\webtestdata\db_tools\importinputtipdata\importexceldata\exceldata\输入框提示测试数据.xls")  #实例化
    readdata.readData()
