from django.shortcuts import render
from django.views.generic import View   #导入View
from django.http import HttpResponse   #导入HttpResponse ，用于指定返回的类型，返回的是json字符串
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger #分页导入包
from django.contrib.auth.models import User #导入引用django默认新建user表的类User

from .models import PageEle,ModulePage   #导入PageEle
from .forms import PageEleForm,ModulePageForm  #导入PageEleForm
from .models import EleTestData,TestProject,ProjectModule,ModulePage,PageEle,EleTestDataType
from .forms import EleTestDataForm


# 添加页面元素
class  PageEleView(View):  #继承View
    """
    测试用例复制编写页面处理
    """
    def get(self,request,pageele_id):
        if request.user.username == 'check':
            return render(request, "NoAddCase.html")
        elif request.user.is_active:
            pageele = PageEle.objects.get(id=int(pageele_id))   #获取用例
            modulepages = ModulePage.objects.all()
            return render(request,"pageele.html",
                          {"pageele":pageele,
                           "modulepages": modulepages,
                           })
        else:
            return render(request,"addcaseError.html")

    def post(self, request,pageele_id):
        username = request.user.username
        pageele_form = PageEleForm(request.POST)  # 实例化pageeleFrom()
        pageele = PageEle.objects.get(id=int(pageele_id))  # 获取用例
        modulepages = ModulePage.objects.all()

        if pageele_form.is_valid():  # is_valid()判断是否有错

            pageele_form.save(commit=True)  # 将信息保存到数据库中

            # zj = QSpageele.objects.all().order_by('-id')[:1][0]   #根据id查询最新的
            zj = PageEle.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            # user = User.objects.get(username=username)
            # zj.write_user_id = user.id
            zj.save()

            # #判断新加的用例的项目名称和模块名称是否是新的，是新的就在CaseReport模块中新加，不是就不加
            # casereports = CaseReport.objects.all()  # 获取CaseReport所用内容
            # casereport_project_name_list = []
            # casereport_module_name_list = []
            # for casereport in casereports:
            #     casereport_project_name_list.append(casereport.test_project)  # 将CaseReport中所有项目名保存在一个列表里
            #     casereport_module_name_list.append(casereport.test_module)  # 将CaseReport中所有模块名保存在一个列表里
            # 
            # if zj.test_project not in casereport_project_name_list:  # 如果新加用例的项目名不在CaseReport项目中，则新加一条数据
            #     newcasereport = CaseReport()
            #     newcasereport.test_project = zj.test_project
            #     newcasereport.test_module = zj.test_module
            #     newcasereport.save()
            # elif zj.test_module not in casereport_module_name_list:
            #     newcasereport = CaseReport()
            #     newcasereport.test_project = zj.test_project
            #     newcasereport.test_module = zj.test_module
            #     newcasereport.save()


            pageeleid = zj.id
            # qstesecase_id = int(qstesecase_id) +1
            pageeleadd = PageEle.objects.get(id=int(pageeleid))  # 获取用例
            return render(request, "pageele.html", {
                "pageele": pageeleadd,
                "modulepages": modulepages,
                "sumsg":u"添加---【{}】---成功,请继续添加".format(pageeleadd.ele_name),
            })
        else:
            return render(request, 'pageeleform.html', {
                "pageele": pageele,
                "pageeleform": pageele_form,
                "modulepages": modulepages,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写或是否已添加过",
            })  # 返回页面，回填信息


#模块页面view
class  ModulePageView(View):  #继承View
    """
    测试用例复制编写页面处理
    """
    def get(self,request,modulepage_id):
        if request.user.username == 'check':
            return render(request, "NoAddCase.html")
        elif request.user.is_active:
            modulepage = ModulePage.objects.get(id=int(modulepage_id))   #获取用例
            testprojects = TestProject.objects.all()
            projectmodules = ProjectModule.objects.all()
            # modulepages = ModulePage.objects.all()
            # pageeles = PageEle.objects.all()
            # eletestdatatypes = EleTestDataType.objects.all()

            return render(request,"modulepage.html",{
                "modulepage":modulepage,
                "testprojects": testprojects,
                "projectmodules": projectmodules,
                # "modulepages": modulepages,
                # "pageeles": pageeles,
                # "eletestdatatypes": eletestdatatypes,
            })
        else:
            return render(request,"addcaseError.html")

    def post(self, request,modulepage_id):
        username = request.user.username
        modulepage_form = ModulePageForm(request.POST)  # 实例化pageeleFrom()
        modulepage = ModulePage.objects.get(id=int(modulepage_id))  # 获取用例

        testprojects = TestProject.objects.all()
        projectmodules = ProjectModule.objects.all()
        # modulepages = ModulePage.objects.all()
        # pageeles = PageEle.objects.all()
        # eletestdatatypes = EleTestDataType.objects.all()

        if modulepage_form.is_valid():  # is_valid()判断是否有错

            modulepage_form.save(commit=True)  # 将信息保存到数据库中

            # zj = QSpageele.objects.all().order_by('-id')[:1][0]   #根据id查询最新的
            zj = ModulePage.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            # user = User.objects.get(username=username)
            # zj.write_user_id = user.id
            zj.save()

            # #判断新加的用例的项目名称和模块名称是否是新的，是新的就在CaseReport模块中新加，不是就不加
            # casereports = CaseReport.objects.all()  # 获取CaseReport所用内容
            # casereport_project_name_list = []
            # casereport_module_name_list = []
            # for casereport in casereports:
            #     casereport_project_name_list.append(casereport.test_project)  # 将CaseReport中所有项目名保存在一个列表里
            #     casereport_module_name_list.append(casereport.test_module)  # 将CaseReport中所有模块名保存在一个列表里
            #
            # if zj.test_project not in casereport_project_name_list:  # 如果新加用例的项目名不在CaseReport项目中，则新加一条数据
            #     newcasereport = CaseReport()
            #     newcasereport.test_project = zj.test_project
            #     newcasereport.test_module = zj.test_module
            #     newcasereport.save()
            # elif zj.test_module not in casereport_module_name_list:
            #     newcasereport = CaseReport()
            #     newcasereport.test_project = zj.test_project
            #     newcasereport.test_module = zj.test_module
            #     newcasereport.save()

            modulepageid = zj.id
            # qstesecase_id = int(qstesecase_id) +1
            modulepageadd = ModulePage.objects.get(id=int(modulepageid))  # 获取用例
            return render(request, "modulepage.html", {
                "modulepage": modulepageadd,
                "testprojects": testprojects,
                "projectmodules": projectmodules,
                # "modulepages": modulepages,
                # "pageeles": pageeles,
                # "eletestdatatypes": eletestdatatypes,
                "sumsg":u"添加---【{}】---成功,请继续添加".format(modulepageadd.ele_page),
            })
        else:
            # return render(request, "modulepage.html", {
            #     "modulepage": modulepage,
            #     "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
            # })  # 返回页面，回填信息
            return render(request, "modulepageform.html", {
                "modulepage": modulepage,
                "modulepageform": modulepage_form,
                "testprojects": testprojects,
                "projectmodules": projectmodules,
                # "modulepages": modulepages,
                # "pageeles": pageeles,
                # "eletestdatatypes": eletestdatatypes,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写或是否已添加过",
            })  # 返回页面，回填信息


#元素测试数据view
class  EleTestDataView(View):  #继承View
    """
    测试用例复制编写页面处理
    """
    def get(self,request,eletestdata_id):
        if request.user.username == 'check':
            return render(request, "NoAddCase.html")
        elif request.user.is_active:
            eletestdata = EleTestData.objects.get(id=int(eletestdata_id))   #获取用例
            testprojects = TestProject.objects.all()
            projectmodules = ProjectModule.objects.all()
            modulepages = ModulePage.objects.all()
            pageeles = PageEle.objects.all()
            eletestdatatypes = EleTestDataType.objects.all()

            return render(request,"eletestdata.html",
                          {"eletestdata":eletestdata,
                           "testprojects":testprojects,
                           "projectmodules":projectmodules,
                           "modulepages":modulepages,
                           "pageeles":pageeles,
                           "eletestdatatypes":eletestdatatypes,
                           })
        else:
            return render(request,"addcaseError.html")

    def post(self, request,eletestdata_id):
        username = request.user.username
        eletestdata_form = EleTestDataForm(request.POST)  # 实例化EleTestDataForm()
        eletestdata =EleTestData.objects.get(id=int(eletestdata_id))  # 获取用例
        testprojects = TestProject.objects.all()
        projectmodules = ProjectModule.objects.all()
        modulepages = ModulePage.objects.all()
        pageeles = PageEle.objects.all()
        eletestdatatypes = EleTestDataType.objects.all()

        if eletestdata_form.is_valid():  # is_valid()判断是否有错

            eletestdata_form.save(commit=True)  # 将信息保存到数据库中

            # zj = QSpageele.objects.all().order_by('-id')[:1][0]   #根据id查询最新的
            zj = EleTestData.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            # user = User.objects.get(username=username)
            # zj.write_user_id = user.id
            zj.save()

            # #判断新加的用例的项目名称和模块名称是否是新的，是新的就在CaseReport模块中新加，不是就不加
            # casereports = CaseReport.objects.all()  # 获取CaseReport所用内容
            # casereport_project_name_list = []
            # casereport_module_name_list = []
            # for casereport in casereports:
            #     casereport_project_name_list.append(casereport.test_project)  # 将CaseReport中所有项目名保存在一个列表里
            #     casereport_module_name_list.append(casereport.test_module)  # 将CaseReport中所有模块名保存在一个列表里
            #
            # if zj.test_project not in casereport_project_name_list:  # 如果新加用例的项目名不在CaseReport项目中，则新加一条数据
            #     newcasereport = CaseReport()
            #     newcasereport.test_project = zj.test_project
            #     newcasereport.test_module = zj.test_module
            #     newcasereport.save()
            # elif zj.test_module not in casereport_module_name_list:
            #     newcasereport = CaseReport()
            #     newcasereport.test_project = zj.test_project
            #     newcasereport.test_module = zj.test_module
            #     newcasereport.save()

            eletestdataid = zj.id
            # qstesecase_id = int(qstesecase_id) +1
            eletestdataadd = EleTestData.objects.get(id=int(eletestdataid))  # 获取用例


            return render(request, "eletestdata.html", {
                "eletestdata": eletestdataadd,
                "testprojects": testprojects,
                "projectmodules": projectmodules,
                "modulepages": modulepages,
                "pageeles": pageeles,
                "eletestdatatypes": eletestdatatypes,
                "sumsg":u"添加---【{}】---成功,请继续添加".format(eletestdataadd.test_data),
            })
        else:
            # return render(request, "modulepage.html", {
            #     "modulepage": modulepage,
            #     "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
            # })  # 返回页面，回填信息
            return render(request, "eletestdataform.html", {
                "eletestdata": eletestdata,
                "testprojects": testprojects,
                "projectmodules": projectmodules,
                "modulepages": modulepages,
                "pageeles": pageeles,
                "eletestdatatypes": eletestdatatypes,
                "eletestdataform": eletestdata_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写或是否已添加过",
            })  # 返回页面，回填信息












