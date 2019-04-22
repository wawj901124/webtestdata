from django.db import models

# Create your models here.

class Test(models.Model):
    """测试学习用"""
    Auto = models.AutoField()    #自增长型
    BigAuto= models.BigAutoField   #大数值自增长型

    #二进制数据
    Binary = models.BinaryField()

    #布尔型
    Boolean = models.BooleanField()
    NullBoolean = models.NullBooleanField()   #可以为空的布尔型

    #整型
    PositiveSmallInteger = models.PositiveSmallIntegerField(db_column="age")   #5个字节的小型整数,db_column定义数据库中对应的字段的名字
    SmallInteger = models.SmallIntegerField(primary_key=False)   #6个字节的小型整数,primary_key定义是否主键（主键的特性是要唯一，False说明是非主键）
    PositiveInteger = models.PositiveIntegerField()   # 10个字节的正整数
    Integer= models.IntegerField(verbose_name="11个字节大小")   #11个字节的整数,verbose_name定义字段注释
    BigInteger = models.BigIntegerField(unique=True)   #大型整数,unique=True,表示值唯一

    #字符串类型
    Char = models.CharField(max_length=100,null=True,blank=True,db_index=True)   #有长度限制字符型,max_length=100,表示字符段长度为100，null=True表示数据中可以为空，
                                                                                    #blank=True表示前端页面的输入值可以为空，db_index=True表示建立索引值
    Text = models.TextField(help_text="这个是longtext")   #无长度限制字符串型，help_text="这个是longtext"定义字段的说明

    #时间日期类型
    Date = models.DateField(unique_for_date=True,auto_now=True)   #年月日,unique_for_date=True表示日唯一，auto_now=True表示更新时间为此字段
    DateTime = models.DateTimeField(editable=False,unique_for_month=True,auto_now_add=True)   #年月日时分秒,editable=False表示该字段可编辑,unique_for_month=True表示月唯一，
                                                                                                #auto_now_add=True表示创建时间为此字段
    Duration = models.DurationField()   #某个时间段的时间，例如某个月，某年

    #浮点型
    Float = models.FloatField()   #浮点类型数据
    Decimal= models.DecimalField(max_digits=4,decimal_places=2)   #定义浮点类型，可以定义总位数（max_digits）和小数点后的位数（decimal_places）,max_digits=4表示整个位数为4位，
                                                                    # decimal_places=2表示小数点后位数为2位

    #其他字段
    Email = models.EmailField()   #邮箱
    Image = models.ImageField()   #图片类型，可以定义宽度（width_field）和高度（height_field）
    File = models.FileField()   #文件类型，可以定义上传位置（upload_to）
    FilePath = models.FilePathField()   #文件路径类型
    URL = models.URLField()   #URL类型
    UUID = models.UUIDField()   #UUID类型
    GenericIPAddress = models.GenericIPAddressField()   #IP地址类型


class A(models.Model):
    onetoone = models.OneToOneField(Test,related_name="one") #一对一类型，related_name="one"表示关联名字为one

class B(models.Model):
    foreign = models.ForeignKey(A,on_delete=models.CASCADE)   #一对多，外键，删除级联，表示筛选字段，与该字段相关的外键引用的类容都删除，
                                                                             # 例如删除某个老师，老师名下的所有课程都被删除
    foreign1 = models.ForeignKey(A,on_delete=models.PROTECT)   #表示删除某个关联数据时，会报错，例如直接删除老师，老师的课程还在，会报错，删除不了老师
    foreign2 = models.ForeignKey(A,on_delete=models.SET_NULL,null=True,blank=True)  #删除置空，使用models.SET_NULL，必须要加null=True,blank=True
                                                                                    #例如，删除某个老师，这个老师的助教不一定删除，要置空放置
    foreign3 = models.ForeignKey(A,on_delete=models.SET_DEFAULT,default=0)   #删除置为默认值，使用models.SET_DEFAULT，必须要有设置default的值（default=0）
    foreign4 = models.ForeignKey(A,on_delete=models.DO_NOTHING)     #删除外键后，此字段值依然保留，什么也不做
    foreign5 = models.ForeignKey(A,on_delete=models.SET)  #删除后置为SET函数所设置的值

    """
    on_delete 当一个被外键关联的对象被删除时，Django将模仿on_delete参数定义的SQL约束执行相应操作
        如下6中操作
        CASCADE：模拟SQL语言中的ON DELETE CASCADE约束，将定义有外键的模型对象同时删除（该操作作为当前Django版本的默认操作）
        PROTECT：阻止上面的删除操作，弹出ProtectedError异常
        SET_NULL：将外键字段设为null,只有当字段设置了null=True时，方可使用该值
        SET_DEFAULT：将外键字段设为默认值，只有当字段设置了Default参数时，方可使用
        DO_NOTHING：什么也不做
        SET()：设置为一个传递给SET（）的值或者一个回调函数的返回值。注意大小写
    """

class AddressInfo(models.Model): #coures_addressinfo
    """省市县地址信息"""
    address = models.CharField(max_length=200,null=True,blank=True,verbose_name="地址")
    pid = models.ForeignKey('self',null=True,blank=True,verbose_name="自关联")   #使用self，进行自关联
    note = models.CharField(max_length=200,null=True,blank=True,verbose_name="说明")

    def __str__(self):   #__unicode__(self)
        return self.address   #返回显示的内容

    class Meta:
        #定义元数据
        db_table = 'address'  #定义表格的名字，不会按照django默认的名字方式来命名表格
        ordering = ['pid']   #指定按照什么字段排序，加-表示反向排序，不加-表示正序
        get_latest_by = ['pid']   #按照某个字段，获取最近和最开始的数据
        verbose_name = '省市县地址信息'  #定义说明
        verbose_name_plural = verbose_name   #定义复数形式，不定义，默认为s
        abstract = True  #表示
        permissions = (('定义好的权限','权限说明'),)   #定义权限
        managed = False  #表示是否新建表
        unique_together = ('adddress','note')   #表示多个字段联合唯一 #（（）,（））
        app_label = 'courses'  #表示是哪个应用下的表，表示为courses应用下的表
        db_tablespace = 'addr'   #定义数据库表空间的名字


class Course(models.Model):
    """课程信息表"""
    title = models.CharField(max_length=200,null=True,blank=True,verbose_name="地址")
    type = models.CharField(choices=((1,'实战课'),(2,'免费课'),(0,'其它')),max_length=1,default=0,verbose_name="课程类型")
    price = models.PositiveSmallIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        verbose_name = "课程信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.get_type_display()}-{self.title}"   #使用f表示格式化数据，python6的心特性，低版本不能使用
        # return "{}-{}" .format(self.get_type_display(),self.title)  #示例：实战课-Django零基础入门到实战

class Student(models.Model):
    """学生信息表"""
    nickname =  models.CharField(max_length=30,primary_key=True,null=True,blank=True,verbose_name="昵称")
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.CharField(choices=((1,'男'),(2,'女'),(0,'保密')),max_length=1,default=0,verbose_name="性别")
    study_time = models.PositiveIntegerField(default='0',verbose_name="学习时长（h）")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        verbose_name = "学生信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

class Teacher(models.Model):
    """教师信息表"""
    nickname =  models.CharField(max_length=30,primary_key=True,null=True,blank=True,verbose_name="昵称")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        verbose_name = "教师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

class TeacherAssistant(models.Model):
    """助教信息表"""
    nickname =  models.CharField(max_length=30,primary_key=True,null=True,blank=True,verbose_name="昵称")
    teacher = models.OneToOneField(Teacher, null=True,blank=True,on_delete=models.SET_NULL,verbose_name="讲师")   #删除置空
    hobby = models.CharField(max_length=100,primary_key=True,null=True,blank=True,verbose_name="爱好")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        verbose_name = "助教信息表"
        db_table = 'courses_asssistant'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

#删除表中的内容：
    #1.先删除models.py中的相应的Class，
    #2.删除对应的migrations中的文件
    #3.删除数据库中djang_migration表中的相应记录
    #4.删除数据库中对应的表，例如表'courses_asssistant'

#导入数据
    #1.python manage.py shell  #进入
    #2.写py文件进行导入
    #3.使用数据库层面的数据导入
#导出数据
    #1.使用数据库层面的导出数据




