from django.urls import path

from .views import TestSearchView



urlpatterns = [
    #相同参数的路径名一定不能一样。比如copy/<path:testcase_id>/与<path:testcase_id>/不能并列存在
    path('testsearchcopy/<path:testsearch_id>/', TestSearchView.as_view(), name="test_search_id"),  # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定
    # path('modulepagecopy/<path:modulepage_id>/', ModulePageView.as_view(), name="module_page_id"),  # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定
    # path('eletestdatacopy/<path:eletestdata_id>/', EleTestDataView.as_view(), name="ele_test_data_id"),  # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

]

app_name = 'testfundata'