from django.shortcuts import render
from django.views.generic import View   #导入View

from .forms import TestSearchForm
from .models import TestSearch
from pageelement.models import ModulePage,PageEle
# Create your views here.
#元素测试数据view
class  TestSearchView(View):  #继承View
    """
    测试用例复制编写页面处理
    """
    def get(self,request,testsearch_id):
        if request.user.username == 'check':
            return render(request, "NoAddCase.html")
        elif request.user.is_active:
            testsearch = TestSearch.objects.get(id=int(testsearch_id))   #获取用例
            # testprojects = TestProject.objects.all()
            # projectmodules = ProjectModule.objects.all()
            modulepages = ModulePage.objects.all()
            pageeles = PageEle.objects.all()
            # eletestdatatypes = EleTestDataType.objects.all()

            return render(request,"testsearch.html",
                          {"testsearch":testsearch,
                           # "testprojects":testprojects,
                           # "projectmodules":projectmodules,
                           "modulepages":modulepages,
                           "pageeles":pageeles,
                           # "eletestdatatypes":eletestdatatypes,
                           })
        else:
            return render(request,"addcaseError.html")

    def post(self, request,testsearch_id):
        username = request.user.username
        testsearch_form = TestSearchForm(request.POST)  # 实例化EleTestDataForm()
        testsearch =TestSearch.objects.get(id=int(testsearch_id))  # 获取用例
        # testprojects = TestProject.objects.all()
        # projectmodules = ProjectModule.objects.all()
        modulepages = ModulePage.objects.all()
        pageeles = PageEle.objects.all()
        # eletestdatatypes = EleTestDataType.objects.all()

        if testsearch_form.is_valid():  # is_valid()判断是否有错

            testsearch_form.save(commit=True)  # 将信息保存到数据库中

            # zj = QSpageele.objects.all().order_by('-id')[:1][0]   #根据id查询最新的
            zj = TestSearch.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
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

            testsearchid = zj.id
            # qstesecase_id = int(qstesecase_id) +1
            testsearchadd = TestSearch.objects.get(id=int(testsearchid))  # 获取用例


            return render(request, "testsearch.html", {
                "testsearch": testsearchadd,
                # "testprojects": testprojects,
                # "projectmodules": projectmodules,
                "modulepages": modulepages,
                "pageeles": pageeles,
                # "eletestdatatypes": eletestdatatypes,
                "sumsg":u"添加---【{}】---成功,请继续添加".format(str(testsearchadd.add_time)),
            })
        else:
            return render(request, "testsearch.html", {
                # "eletestdata": eletestdata,
                # "testprojects": testprojects,
                # "projectmodules": projectmodules,
                # "modulepages": modulepages,
                # "pageeles": pageeles,
                # "eletestdatatypes": eletestdatatypes,
                # "eletestdataform": eletestdata_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写或是否已添加过",
            })  # 返回页面，回填信息
