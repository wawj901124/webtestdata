from django.shortcuts import render
from django.db.models import Count,Avg,Max,Min,Sum,F,Q   #导入技术，求平均值，最大值，最小值，求和
from django.views.generic import View
from django.http import JsonResponse
from .models import AddressInfo,Teacher,Course,Student,TeacherAssistant,GroupConcat   #导入模型

# Create your views here.
#在view中使用函数

class IndexView(View):
    """主页"""
    def get(self,request):
        #1.查询、检索、过滤
        teachers = Teacher.objects.all()
        teacher2 = Teacher.objects.get(nickname='Jack')   #get()只能返回一条结果，多条则会报错
        print(teacher2,type(teacher2))
        teacher3 = Teacher.objects.filter(fans__gte=500)   #粉丝数大于等于500
        for t in teacher3:
            print(f"讲师姓名{t.nickname}--粉丝数{t.fans}")

        #2.字段数据匹配，大小写敏感
        teacher4 = Teacher.objects.filter(fans__in=[666,1231])   #粉丝数数在列出的几个数中
        print(teacher4)
        teacher5 = Teacher.objects.filter(nickname__icontains="A")   #昵称中包含A的，不区分大小写
        print(teacher5)

        #3.结果切片、排序、链式查询
        print(Teacher.objects.all()[:1])   #切片
        teacher6 = Teacher.objects.all().order_by("-fans")   #按fans倒序排列
        for t in teacher6:
            print(t.fans)
        print(Teacher.objects.filter(fans__gte=500).order_by('nickname'))  #链式查询

        #4.查看执行的原生SQL .query
        print(str(Teacher.objects.filter(fans__gte=500).order_by('nickname').query))   #查看原生的SQL语句

        """返回新QuerySet API"""
        #1.all()-全部,filter()-过滤,order_by()-排序,exclude()-不包含某些字段,reverse()-反向排序，要使用此函数model总的meta要定义ordering, distinct()-去重复
        s1 = Student.objects.all().exclude(nickname="A同学")  # 不包含A同学的数据
        for s in s1:
            print(s.nickname,s.age)
        s2 = Student.objects.all().exclude(nickname="A同学").reverse()  # 不包含A同学的数据,反向排序
        for s in s2:
            print(s.nickname,s.age)

        #2.extra()-实现字段别名, defer()-排除一些字段,only()-选择一些字段
        s3 = Student.objects.all().extra(select={"name":"nickname"})  #把字段nickname修改别名为name
        for s in s3:
            print(s.name)
        print(str(Student.objects.all().only('nickname','age').query))   #只显示查询'nickname'和'age'字段内内容，“.query”-查看原生SQL语句

        #3.values()-获取字典形式的QuerySet，values_list()-获取元组形式的QuerySet
        print(TeacherAssistant.objects.values('nickname','hobby'))   #获取字典形式的键为字段名，值为字段值
        print(TeacherAssistant.objects.values_list('nickname','hobby'))   #获取元组形式的键为字段名，值为字段值
        print(TeacherAssistant.objects.values_list('nickname', flat=True))  #  flat=True,表示当只有一个字段时，获取到一个列表形式的

        #4.dates(),datetimes()  根据时间日期获取查询集
        print(Course.objects.dates('creates_at','year',order='DESC'))   #按照creates_at字段，查询nian,DESC表示降序，dates有年月日
        print(Course.objects.datetimes('creates_at', 'year', order='DESC'))  # 按照creates_at字段，查询nian,DESC表示降序，dates有年月日时分秒

        #5.union()-并集,intersection()-交集,difference()-差集   mysql只支持union()查询
        p_240 = Course.objects.filter(price__gte=240)  #价钱大于等于240
        p_260 = Course.objects.filter(price__lte=260)   #价钱小于等于260
        print(p_240.union(p_260))   #联合查询
        print(p_240.intersection(p_260))   #取交集
        print(p_240.difference(p_260))   #取差集

        #6.select_related()  一对一、多对一查询优化，prefectch_related() 一对多、多对多查询优化，反向查询
        courses = Course.objects.all().select_related('teacher')
        for c in courses:
            print(f"{c.title}--{c.teacher.nickname}--{c.teacher.fans}")

        students = Student.objects.filter(age__lt=30).prefetch_related('course')
        for s in students:
            print(s.course.all())

        print(Teacher.objects.get(nickname='Jack').course_set.all())   #反向查询

        #7.annotate() 使用聚合计数、求和、平均数 raw() 执行原生的SQL
        print(Course.objects.values('teacher').annotate(vol = Sum('volume')))
        print(Course.objects.values('teacher').annotate(pri = Avg('price')))
        print(Course.objects.values('teacher').raw('SQL语句'))   #执行原生语句

        """不返回QuerySet API"""
        #1.获取对象get(),get_or_create(),first(),last().lastest(),eraliest(),in_bulk()
        print(Course.objects.first())   #第一个
        print(Course.objects.last())   #最后一个
        print(Course.objects.earliest())  #最早一个， 使用时，model中要有get_latest_by字段
        print(Course.objects.latest())   #最近一个，使用时，model中要有get_latest_by字段
        print(Course.objects.in_bulk(['Python系列教程4','Golang系列教程1']))

        #2.创建对象create()-创建, bulk_create()-批量创建, update_or_create()-更新或创建

        #3.更新对象update()-更新，create_or_update()-创建或更新
        Course.objects.filter(title='Java系列教程2').update(price=300)  #更新价格为300

        #4.删除对象delete(),使用filter过滤
        Course.objects.filter(title='test').delete()   #删除title为test的项

        #5.其他操作exists()-判断是否存在,count()-统计个数,aggregate()-聚合
        print(Course.objects.filter(title='test').exists())   #判断title为test的项是否存在
        print(Course.objects.filter(title='Java系列教程2').exists())   #判断title为'Java系列教程2'的项是否存在
        print(Course.objects.count())   #计数
        print(Course.objects.aggregate(Max('price'),Min('price'),Avg('price'),Sum('volume')))   #aggregate与annotate的区别：aggregate计算表中所有数据，annotate是筛选出某些字典集合后

        #6.自定义聚合查询
        courses = Course.objects.values('teacher').annotate(t=GroupConcat('title',
                                                                          distinct=True,
                                                                          ordering='title ASC',   #ASC表示正序
                                                                          separator='-'
                                                                          ))
        for c in courses:
            print(c)


        #F和Q的运用
        Course.objects.update(price=F('price')-11)  #更新表中price字段减11（对表中每一条数据都生效）
        print(Course.objects.filter(volume__lte=F('price')*10))  #过滤出销量小于等于10倍价格的数据
        print(Course.objects.filter(Q(title__icontains='java')& Q(volume__gte=5000)))  #过滤出销量大于等于5000且title内容包含java的数据
        print(Course.objects.filter(Q(title__icontains='golang')| Q(volume__lte=1000)))  #过滤出销量小于等于1000或title内容包含golang的数据






