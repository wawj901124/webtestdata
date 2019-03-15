from django import forms    #导入django中的forms

from .models import PageEle,ModulePage  #导入PageEle模块
from .models import EleTestData


class PageEleForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = PageEle   #指明转换的Model:PageEle
        fields = '__all__' #指明要转换的字段


class ModulePageForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = ModulePage   #指明转换的Model:ModulePage
        fields = '__all__' #指明要转换的字段


class EleTestDataForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = EleTestData   #指明转换的Model:EleTestData
        fields = '__all__' #指明要转换的字段
