# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/5/15 10:19'

from django.contrib.auth.models import User #导入引用django默认新建user表的类User

import xadmin
from xadmin import views   #导入xadmin中的views,用于和 BaseSettings类绑定


from .models import TestProject,ProjectModule,ModulePage,PageEle,EleTestDataType,EleTestData


class TestProjectAdmin(object):
    ziduan = ['web_project',]

    list_display =['id','web_project','add_time']#定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields =  ['web_project',]   #定义搜索字段
    list_filter =  ['web_project',] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['web_project',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['web_project',]   #显示数据详情

    # class ProjectModuleInline(object):
    #     model = ProjectModule
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class ModulePageInline(object):
    #     model = ModulePage
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class PageEleInline(object):
    #     model = PageEle
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class EleTestDataTypeInline(object):
    #     model = EleTestDataType
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class EleTestDataInline(object):
    #     model = EleTestData
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [ProjectModuleInline,ModulePageInline,PageEleInline,EleTestDataTypeInline,EleTestDataInline]

    # class PageTestDataInline(object):
    #     model = PageTestData
    #     # exclude = ["add_time"]
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [PageTestDataInline]


class ProjectModuleAdmin(object):
    ziduan = ['web_module',]

    list_display =['id','web_module','add_time',]#定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields =  ['web_module',]   #定义搜索字段
    list_filter =  ['web_module',] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['web_module',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['web_module',]   #显示数据详情

    # class ProjectModuleInline(object):
    #     model = ProjectModule
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class ModulePageInline(object):
    #     model = ModulePage
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class PageEleInline(object):
    #     model = PageEle
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class EleTestDataTypeInline(object):
    #     model = EleTestDataType
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class EleTestDataInline(object):
    #     model = EleTestData
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [ModulePageInline,PageEleInline,EleTestDataTypeInline,EleTestDataInline]

    # class PageTestDataInline(object):
    #     model = PageTestData
    #     # exclude = ["add_time"]
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [PageTestDataInline]


class ModulePageAdmin(object):
    ziduan = ['testproject','projectmodule','ele_page','ele_page_url']

    list_display =['id','testproject','projectmodule','ele_page','ele_page_url','add_time','go_to']#定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields =  ['testproject','projectmodule','ele_page','ele_page_url']   #定义搜索字段
    list_filter =  ['testproject','projectmodule','ele_page','ele_page_url'] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['ele_page',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['ele_page',]   #显示数据详情

    # class ProjectModuleInline(object):
    #     model = ProjectModule
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class ModulePageInline(object):
    #     model = ModulePage
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class PageEleInline(object):
    #     model = PageEle
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class EleTestDataTypeInline(object):
    #     model = EleTestDataType
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class EleTestDataInline(object):
    #     model = EleTestData
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [PageEleInline,EleTestDataTypeInline,EleTestDataInline]


class PageEleAdmin(object):
    ziduan = ['modulepage','ele_name','ele_xpath']

    list_display =['id','modulepage','ele_name','ele_xpath','add_time','go_to']#定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields =  ['modulepage','ele_name','ele_xpath']   #定义搜索字段
    list_filter =  ['modulepage','ele_name','ele_xpath'] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['ele_name',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['ele_name',]   #显示数据详情

    # class ProjectModuleInline(object):
    #     model = ProjectModule
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class ModulePageInline(object):
    #     model = ModulePage
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class PageEleInline(object):
    #     model = PageEle
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class EleTestDataTypeInline(object):
    #     model = EleTestDataType
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # class EleTestDataInline(object):
    #     model = EleTestData
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [EleTestDataTypeInline,EleTestDataInline]


class EleTestDataTypeAdmin(object):
    ziduan = ['test_data_type']

    list_display =['id','test_data_type','add_time']#定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields =  ['test_data_type']   #定义搜索字段
    list_filter =  ['test_data_type'] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_data_type',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_data_type',]   #显示数据详情

    # class ProjectModuleInline(object):
    #     model = ProjectModule
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class ModulePageInline(object):
    #     model = ModulePage
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class PageEleInline(object):
    #     model = PageEle
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class EleTestDataTypeInline(object):
    #     model = EleTestDataType
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class EleTestDataInline(object):
    #     model = EleTestData
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [EleTestDataInline]


class EleTestDataAdmin(object):
    ziduan = ['pageele','eletestdatatype','test_data']

    list_display =['id','pageele','eletestdatatype','test_data','add_time','go_to']#定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields =  ['pageele','eletestdatatype','test_data']   #定义搜索字段
    list_filter =  ['pageele','eletestdatatype','test_data'] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_data',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_data',]   #显示数据详情

    # class ProjectModuleInline(object):
    #     model = ProjectModule
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class ModulePageInline(object):
    #     model = ModulePage
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class PageEleInline(object):
    #     model = PageEle
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class EleTestDataTypeInline(object):
    #     model = EleTestDataType
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'

    # class EleTestDataInline(object):
    #     model = EleTestData
    #     exclude = ["add_time"]   #不展示某个字段
    #     extra = 1
    #     style = 'tab'
    #
    # inlines = [EleTestDataInline]

xadmin.site.register(TestProject, TestProjectAdmin) #在xadmin中注册TestProject
xadmin.site.register(ProjectModule, ProjectModuleAdmin) #在xadmin中注册ProjectModule
xadmin.site.register(ModulePage, ModulePageAdmin) #在xadmin中注册ModulePage
xadmin.site.register(PageEle, PageEleAdmin) #在xadmin中注册PageEle
xadmin.site.register(EleTestDataType, EleTestDataTypeAdmin) #在xadmin中注册PageEle
xadmin.site.register(EleTestData, EleTestDataAdmin) #在xadmin中注册PageEle

# class ModulePageAdmin(object):
#     ziduan = ['web_project','web_module','ele_page','ele_page_url']
#
#
#     list_display =['id','web_project','web_module','ele_page','ele_page_url','add_page_time','go_to']#定义显示的字段
#
#     # list_display =[ 'test_project','test_module',
#     #                 'case_title',
#     #           ] #定义显示的字段
#     search_fields =  ['web_project','web_module','ele_page','ele_page_url']   #定义搜索字段
#     list_filter =  ['web_project','web_module','ele_page','ele_page_url'] #定义筛选的字段
#     model_icon = 'fa fa-tasks'  # 定义图标显示
#     ordering = ['-add_page_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
#     readonly_fields = ['add_page_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
#     # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
#     # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
#     list_editable = ziduan   # 可以在列表页对字段进行编辑
#     refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
#     list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
#     # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
#     list_display_links = ['web_project',]   #设置点击链接进入编辑页面的字段
#     # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
#     show_detail_fields = ['web_project',]   #显示数据详情
#
#     class PageEleInline(object):
#         model = PageEle
#         exclude = ["add_time"]   #不展示某个字段
#         extra = 1
#         style = 'tab'
#
#     class EleTestDataInline(object):
#         model = EleTestData
#         exclude = ["add_time"]   #不展示某个字段
#         extra = 1
#         style = 'tab'
#
#
#     inlines = [PageEleInline,EleTestDataInline]
#
#     # class PageTestDataInline(object):
#     #     model = PageTestData
#     #     # exclude = ["add_time"]
#     #     extra = 1
#     #     style = 'tab'
#     #
#     # inlines = [PageTestDataInline]


# class PageTestDataAdmin(object):
#     ziduan = ['modulepage','test_title','test_ele','test_ele_data']
#
#
#     list_display =['id','modulepage','test_title','test_ele','test_ele_data','add_time',]#定义显示的字段
#
#     # list_display =[ 'test_project','test_module',
#     #                 'case_title',
#     #           ] #定义显示的字段
#     search_fields =  ['modulepage','test_title','test_ele','test_ele_data']   #定义搜索字段
#     list_filter =  ['modulepage','test_title','test_ele','test_ele_data'] #定义筛选的字段
#     model_icon = 'fa fa-tasks'  # 定义图标显示
#     ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
#     readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
#     # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
#     # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
#     list_editable = ziduan   # 可以在列表页对字段进行编辑
#     refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
#     list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
#     # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
#     list_display_links = ['modulepage',]   #设置点击链接进入编辑页面的字段
#     # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
#     show_detail_fields = ['modulepage',]   #显示数据详情

# xadmin.site.register(TestProject, TestProjectAdmin) #在xadmin中注册TestProject
# xadmin.site.register(ModulePage, ModulePageAdmin) #在xadmin中注册ModulePage
# xadmin.site.register(PageTestData, PageTestDataAdmin) #在xadmin中注册PageTestData




class BaseSettings(object):   #全站的配置类, 配置主题
    enable_themes = True  #主题功能,enable_themes=True 表示要使用它的主题功能，xadmin默认是取消掉的
    use_bootswatch = True   #xadmin默认是取消掉的

xadmin.site.register(views.BaseAdminView, BaseSettings)   #注册BaseSettings


class GlobalSettings(object):   ##全站的配置类
    site_title = "印尼测试后台管理系统"   #页面左上角的标题名称
    site_footer = "爱贝测试网"   #页面底部的文字显示内容
    menu_style = "accordion"  # 将一个app下的内容收起来

xadmin.site.register(views.CommAdminView, GlobalSettings)   #注册GlobalSettings