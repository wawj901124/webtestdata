# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/5/15 10:19'

from django.contrib.auth.models import User #导入引用django默认新建user表的类User

import xadmin
from xadmin import views   #导入xadmin中的views,用于和 BaseSettings类绑定


from .models import  MeminfoTestCase,MeminfoTestResult


class MeminfoTestCaseAdmin(object):
    ziduan = ['testproject', 'testmodule','testpage','testcasetitle',
              'currentpagetext','currrentfindstyle','currentstyleparame','nextpagetext','forcount','dependcase',]

    list_display =['id','testproject', 'testmodule','testpage','testcasetitle',
                   'currentpagetext','currrentfindstyle','currentstyleparame', 'nextpagetext', 'forcount',
                   'dependcase',
                   'add_time','update_time']#定义显示的字段
    search_fields =  ['testproject',]   #定义搜索字段
    list_filter =  ['testproject',] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['testproject',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['testproject',]   #显示数据详情


class MeminfoTestResultAdmin(object):
    ziduan = ['testproject', 'testmodule','testpage','testcasetitle','teststarttime',
              'forcount',
              'currentpagepsstotal', 'currentpageheapsize', 'currentpageheapalloc',
              'currentpageheapfree', 'currentpageobjectsviews', 'currentpageobjectsactivities',
              'currentpageaftertenpsstotal', 'currentpageaftertenheapsize', 'currentpageaftertenheapalloc',
              'currentpageaftertenheapfree', 'currentpageaftertenobjectsviews', 'currentpageaftertenobjectsactivities',
              'clicknextpagepsstotal', 'clicknextpageheapsize', 'clicknextpageheapalloc',
              'clicknextpageheapfree', 'clicknextpageobjectsviews', 'clicknextpageobjectsactivities',
              'nextaftertenpsstotal', 'nextaftertenheapsize', 'nextaftertenheapalloc',
              'nextaftertenheapfree', 'nextaftertenobjectsviews', 'nextaftertenobjectsactivities',
              'nextaftertentwopsstotal', 'nextaftertentwoheapsize', 'nextaftertentwoheapalloc',
              'nextaftertentwoheapfree', 'nextaftertentwoobjectsviews', 'nextaftertentwoobjectsactivities',
              'clickbackpsstotal', 'clickbackheapsize', 'clickbackheapalloc',
              'clickbackheapfree', 'clickbackobjectsviews', 'clickbackobjectsactivities',
              'backaftertenpsstotal', 'backaftertenheapsize', 'backaftertenheapalloc',
              'backaftertenheapfree', 'backaftertenobjectsviews', 'backaftertenobjectsactivities',
              'backaftertentwopsstotal', 'backaftertentwoheapsize', 'backaftertentwoheapalloc',
              'backaftertentwoheapfree', 'backaftertentwoobjectsviews', 'backaftertentwoobjectsactivities',
              'test_phone_name',
              'test_app_packagename',
              'test_app_version',
              ]
    ziduan_all = ['id','testproject', 'testmodule','testpage','testcasetitle','teststarttime',
                    'forcount',
                  'currentpagepsstotal','currentpageheapsize','currentpageheapalloc',
                  'currentpageheapfree','currentpageobjectsviews','currentpageobjectsactivities',
                  'currentpageaftertenpsstotal','currentpageaftertenheapsize','currentpageaftertenheapalloc',
                  'currentpageaftertenheapfree','currentpageaftertenobjectsviews','currentpageaftertenobjectsactivities',
                  'clicknextpagepsstotal','clicknextpageheapsize','clicknextpageheapalloc',
                  'clicknextpageheapfree','clicknextpageobjectsviews','clicknextpageobjectsactivities',
                  'nextaftertenpsstotal','nextaftertenheapsize','nextaftertenheapalloc',
                  'nextaftertenheapfree','nextaftertenobjectsviews','nextaftertenobjectsactivities',
                  'nextaftertentwopsstotal','nextaftertentwoheapsize','nextaftertentwoheapalloc',
                  'nextaftertentwoheapfree','nextaftertentwoobjectsviews','nextaftertentwoobjectsactivities',
                  'clickbackpsstotal','clickbackheapsize','clickbackheapalloc',
                  'clickbackheapfree','clickbackobjectsviews','clickbackobjectsactivities',
                  'backaftertenpsstotal','backaftertenheapsize','backaftertenheapalloc',
                  'backaftertenheapfree','backaftertenobjectsviews','backaftertenobjectsactivities',
                  'backaftertentwopsstotal','backaftertentwoheapsize','backaftertentwoheapalloc',
                  'backaftertentwoheapfree','backaftertentwoobjectsviews','backaftertentwoobjectsactivities',
                   'test_phone_name',
                   'test_app_packagename',
                   'test_app_version',
                   'add_time','update_time']  #定义只读字段

    list_display = ziduan_all#定义显示的字段
    search_fields =  ['testproject', ]   #定义搜索字段
    list_filter =  ['testproject','testmodule','testpage','testcasetitle',
                    'test_phone_name','test_app_packagename','test_app_version',] #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ziduan_all  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # readonly_fields = ['add_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['testproject',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['testproject',]   #显示数据详情
    list_export = ('xls',)  #控制列表页导出数据的可选格式
    show_bookmarks = True   #控制是否显示书签功能
    # data_charts = ""    #控制显示图标的样式
    data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
                      # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
                      #使用网址：https://www.jianshu.com/p/6201e1e9133c
        "user_count": {'title': u"当前页内存统计", "x-field": "forcount", "y-field": ('currentpageheapsize','currentpageaftertenheapsize',),
                       "order": ('id',)},
        "avg_count": {'title': u"进入下一页内存统计", "x-field": "forcount", "y-field": ('clicknextpageheapsize','nextaftertenheapsize','nextaftertentwoheapsize',),
                      "order": ('id',)},
        "back_count": {'title': u"返回当前页内存统计", "x-field": "forcount","y-field": ('clickbackheapsize','backaftertenheapsize','backaftertentwoheapsize',),
                       "order": ('id',)},
        "beforeandafter_count": {'title': u"进入其它页前后当前页内存统计", "x-field": "forcount",
                       "y-field": ('currentpageaftertenheapsize', 'backaftertentwoheapsize',),
                       "order": ('id',)},
    }


xadmin.site.register(MeminfoTestCase, MeminfoTestCaseAdmin) #在xadmin中注册MeminfoTestCase
xadmin.site.register(MeminfoTestResult, MeminfoTestResultAdmin) #在xadmin中注册MeminfoTestResult


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