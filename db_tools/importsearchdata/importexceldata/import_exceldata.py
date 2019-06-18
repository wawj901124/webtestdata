#独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","webtestdata.settings")

import django
django.setup()

from searchdata.models import SearchData

from db_tools.importsearchdata.importexceldata.dataconfig.get_exceldata import GetData


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
            searchdata = SearchData()    #数据库的对象等于SearchData,实例化
            searchdata.webproject = self.exceldata.get_webproject(i)   #填写web后台项目
            searchdata.testpage = self.exceldata.get_testpage(i)    #填写测试页面
            searchdata.testcasetitle = self.exceldata.get_testcasetitle(i)  # 填写测试内容的名称
            searchdata.isclicklastpage = self.exceldata.get_isclicklastpage(i)   #填写是否点击最后一页页码
            searchdata.selectxpath = self.exceldata.get_selectxpath(i)   #填写筛选字段选项Xpath路径
            searchdata.selectoptiontextxpath = self.exceldata.get_selectoptiontextxpath(i)   #填写筛选字段选项内容Xpath路径
            searchdata.selectinputxpath = self.exceldata.get_selectinputxpath(i)   #填写筛选字段选项对应输入框的Xpath路径
            searchdata.selectinputselectonexpath = self.exceldata.get_selectinputselectonexpath(i)   #填写筛选字段选项对应输入框输入内容后下拉列表第一项的Xpath路径
            searchdata.selectinputtext = self.exceldata.get_selectinputtext(i)   #填写筛选字段选项对应输入框的输入内容
            searchdata.isfind = self.exceldata.get_isfind(i)   #填写筛选结果是否有相应内容
            searchdata.colnum = self.exceldata.get_colnum(i)   #填写搜索结果表格的列数
            searchdata.checktext = self.exceldata.get_checktext(i)  # 填写搜索结果表格的列数对应的预期文本内容
            searchdata.save()  #保存到数据库


if __name__ == "__main__":
    readdata = ReadData(file_name=r"D:\Users\Administrator\PycharmProjects\webtestdata\db_tools\importsearchdata\importexceldata\exceldata\检索测试数据.xls")  #实例化
    readdata.readData()
