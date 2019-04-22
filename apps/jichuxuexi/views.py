from django.shortcuts import render
from django.db.models import Count,Avg,Max,Min,Sum   #导入技术，求平均值，最大值，最小值，求和
from django.views.generic import View
from django.http import JsonResponse
from .models import AddressInfo,Teacher,Course,Student,TeacherAssistant   #导入模型

# Create your views here.
#在view中使用函数

class IndexView(View):
    """主页"""
    def get(self,request):
        #1.查询、检索、过滤
        teachers = Teacher.objects.all()
        teacher2 = Teacher.objects.get(nickname='Jack')   #get()只能返回一条结果，多条则会报错


