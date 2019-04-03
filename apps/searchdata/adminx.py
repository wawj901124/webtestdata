# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/5/15 10:19'

from django.contrib.auth.models import User #导入引用django默认新建user表的类User

import xadmin
from xadmin import views   #导入xadmin中的views,用于和 BaseSettings类绑定


from .models import SearchData


class SearchDataAdmin(object):
    ziduan = ['webproject','testpage','testcasetitle','selectxpath','selectoptiontextxpath','selectinputxpath','selectinputtext',
              'isfind','colnum','checktext']

    list_display =['id','webproject','testpage','testcasetitle','selectxpath','selectoptiontextxpath','selectinputxpath','selectinputtext',
                   'isfind','colnum','checktext','add_time']#定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields =  ['webproject',]   #定义搜索字段
    list_filter =  ['webproject',] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['webproject',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['webproject',]   #显示数据详情


xadmin.site.register(SearchData, SearchDataAdmin) #在xadmin中注册LoginData


# class BaseSettings(object):   #全站的配置类, 配置主题
#     enable_themes = True  #主题功能,enable_themes=True 表示要使用它的主题功能，xadmin默认是取消掉的
#     use_bootswatch = True   #xadmin默认是取消掉的
#
# xadmin.site.register(views.BaseAdminView, BaseSettings)   #注册BaseSettings
#
#
# class GlobalSettings(object):   ##全站的配置类
#     site_title = "印尼测试后台管理系统"   #页面左上角的标题名称
#     site_footer = "爱贝测试网"   #页面底部的文字显示内容
#     menu_style = "accordion"  # 将一个app下的内容收起来
#
# xadmin.site.register(views.CommAdminView, GlobalSettings)   #注册GlobalSettings