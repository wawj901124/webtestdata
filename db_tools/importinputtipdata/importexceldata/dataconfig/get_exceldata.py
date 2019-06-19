# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from db_tools.util.operation_excel import OperationExcel   #导入OperationExcel
from db_tools.importinputtipdata.importexceldata.dataconfig.exceldata_config import  *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化
        self.global_var = GlobalVar()   #实例化


    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取id
    def get_id(self,row):
        col = int(self.global_var.id)  #获取id所在的列数
        id = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return id

    # 获取testproject
    def get_testproject(self,row):
        col = int(self.global_var.testproject)  #获取testproject所在的列数
        testproject = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return testproject

    # 获取testmodule
    def get_testmodule(self,row):
        col = int(self.global_var.testmodule)  #获取testmodule所在的列数
        testmodule = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return testmodule

    #获取testpage
    def get_testpage(self,row):
        col = int(self.global_var.testpage)  #获取testpage所在的列数
        testpage = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return testpage

    # 获取testcasetitle
    def get_testcasetitle(self,row):
        col = int(self.global_var.testcasetitle)  #获取testcasetitle所在的列数
        testcasetitle = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return testcasetitle

    # 获取isinput
    def get_isinput(self,row):
        col = int(self.global_var.isinput)  #获取isinput所在的列数
        isinput = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if isinput == "TRUE":
            return "1"
        elif isinput == "True":
            return "1"
        elif isinput == "true":
            return "1"
        elif isinput == u"是":
            return "1"
        elif isinput == u"输入":
            return "1"
        elif isinput == "FALSE":
            return "0"
        elif isinput == "False":
            return "0"
        elif isinput == "false":
            return "0"
        elif isinput == u"否":
            return "0"
        elif isinput == u"不是":
            return "0"
        elif isinput == u"不输入":
            return "0"
        return isinput


    # 获取inputxpath
    def get_inputxpath(self,row):
        col = int(self.global_var.inputxpath)  #获取inputxpath所在的列数
        inputxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if inputxpath == u"空":
            return None
        elif inputxpath == "":
            return None
        elif inputxpath == " ":
            return None
        return inputxpath

    #获取inputtext
    def get_inputtext(self,row):
        col = int(self.global_var.inputtext)  #获取inputtext所在的列数
        inputtext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if inputtext == u"空":
            return None
        elif inputtext == "":
            return None
        elif inputtext == " ":
            return None
        return inputtext

    # 获取inputtipxpath
    def get_inputtipxpath(self,row):
        col = int(self.global_var.inputtipxpath)  #获取inputtipxpath所在的列数
        inputtipxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if inputtipxpath == u"空":
            return None
        elif inputtipxpath == "":
            return None
        elif inputtipxpath == " ":
            return None
        return inputtipxpath

    # 获取inputtiptext
    def get_inputtiptext(self,row):
        col = int(self.global_var.inputtiptext)  #获取inputtiptext所在的列数
        inputtiptext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if inputtiptext == u"空":
            return None
        elif inputtiptext == "":
            return None
        elif inputtiptext == " ":
            return None
        return inputtiptext

    # # 获取selectinputtext
    # def get_selectinputtext(self,row):
    #     col = int(self.global_var.selectinputtext)  #获取selectinputtext所在的列数
    #     selectinputtext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     if selectinputtext == u"空":
    #         return None
    #     elif selectinputtext == "":
    #         return None
    #     elif selectinputtext == " ":
    #         return None
    #     return selectinputtext
    #
    # #获取isfind
    # def get_isfind(self,row):
    #     col = int(self.global_var.isfind)  #获取isfind所在的列数
    #     isfind = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     if isfind == "TRUE":
    #         return "1"
    #     elif isfind == "True":
    #         return "1"
    #     elif isfind == "true":
    #         return "1"
    #     elif isfind == u"是":
    #         return "1"
    #     elif isfind == u"有":
    #         return "1"
    #     elif isfind == "FALSE":
    #         return "0"
    #     elif isfind == "False":
    #         return "0"
    #     elif isfind == "false":
    #         return "0"
    #     elif isfind == u"否":
    #         return "0"
    #     elif isfind == u"没有":
    #         return "0"
    #     return isfind
    #
    # # 获取colnum
    # def get_colnum(self,row):
    #     col = int(self.global_var.colnum)  #获取colnum所在的列数
    #     colnum = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return colnum
    #
    # # 获取checktext
    # def get_checktext(self,row):
    #     col = int(self.global_var.checktext)  #获取checktext所在的列数
    #     checktext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return checktext

    # # 获取write_comments
    # def get_write_comments(self,row):
    #     col = int(self.global_var.write_comments)  #获取write_comments所在的列数
    #     write_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return write_comments
    #
    # # 获取write_user
    # def get_write_user(self,row):
    #     col = int(self.global_var.write_user)  #获取write_user所在的列数
    #     write_user = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return write_user
    #
    # #获取write_case_time
    # def get_write_case_time(self,row):
    #     col = int(self.global_var.write_case_time)  #获取write_case_time所在的列数
    #     write_case_time = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return write_case_time
    #
    # # 获取ex_result
    # def get_ex_result(self,row):
    #     col = int(self.global_var.ex_result)  #获取ex_result所在的列数
    #     ex_result = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return ex_result
    #
    # #获取write_case_time
    # def get_test_comments(self,row):
    #     col = int(self.global_var.test_comments)  #获取test_comments所在的列数
    #     test_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return test_comments
    #
    # # 获取test_user
    # def get_test_user(self,row):
    #     col = int(self.global_var.test_user)  #获取test_user所在的列数
    #     test_user = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return test_user





if __name__ == '__main__':

    getdata = GetData(file_name=r"D:\Users\Administrator\PycharmProjects\webtestdata\db_tools\importinputtipdata\importexceldata\exceldata\输入框提示测试数据.xls",sheet_id=0)   #实例化
    print('---------------------------')
    rows_count = getdata.get_case_lines()
    for i in range(1, rows_count):  # 循环，但去掉第一个
        url = getdata.get_id(i)
        print(url)



