model_name = "CheckTestCase"

#生成forms:
def make_forms(model_name):
    forms_class = """
# 创建%s的form模型
class %sForm(forms.ModelForm):
    class Meta:
        model = %s  # 指明转换的model
        fields = "__all__"
        """ % (model_name, model_name, model_name)
    print("生成在【forms.py】文件中的内容：")
    print(forms_class)
    return forms_class

#生成urls
def make_urls(model_name):
    urls_path = """    # 复制页面的url配置
    path(
        '%s/<path:%s_id>/',
        %sView.as_view(),
        name="%s_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定
    """ % (model_name.lower(), model_name.lower(), model_name, model_name.lower())

    print("生成在【urls.py】文件中urlpatterns的内容：")
    print(urls_path)
    return urls_path


#生成view
def make_views(model_name):
    view_class = """
# %s复制页面的view
class %sView(View):  # 继承View
    def get(self, request, %s_id):
        if request.user.username == 'check':
            return render(request, "error/canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            %s = %s.objects.get(
                id=int(%s_id))  # 获取用例
            clicktestcase_all = ClickTestCase.objects.all().order_by("-id")
            startpackage_all = StartPackage.objects.all().order_by("-id")
            return render(request, "andoriduilayercopy/%s.html",
                          {"%s": %s,
                           "clicktestcase_all": clicktestcase_all,
                           "startpackage_all": startpackage_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request, "error/addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request, %s_id):
        username = request.user.username
        %s = %s.objects.get(
            id=int(%s_id))  # 获取用例
        clicktestcase_all = ClickTestCase.objects.all().order_by("-id")
        startpackage_all = StartPackage.objects.all().order_by("-id")
        %s_form = %sForm(
            request.POST)  # 实例化%sForm()


        if %s_form.is_valid():  # is_valid()判断是否有错

            %s_form.save(commit=True)  # 将信息保存到数据库中

            zj = %s.objects.all().order_by(
                '-add_time')[:1][0]  # 根据添加时间查询最新的
            # user = User.objects.get(username=username)
            # zj.write_user_id = user.id
            # zj.save()

            %sid = zj.id
            %sadd = %s.objects.get(
                id=int(%sid))  # 获取用例
            return render(request, "andoriduilayercopy/%s.html", {
                "%s": %sadd,
                "clicktestcase_all": clicktestcase_all,
                "startpackage_all": startpackage_all,
                "sumsg": u"添加测试用例---【{}】---成功,请继续添加".format(%sadd.testcasetitle),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request,
                          'andoriduilayercopy/%sForm.html',
                          {"%s": %s,
                           "clicktestcase_all": clicktestcase_all,
                           "startpackage_all": startpackage_all,
                           "%sform": %s_form,
                           "errmsg": u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })  # 返回页面，回填信息
    """ % (model_name,model_name,
           model_name.lower(),model_name.lower(),
           model_name, model_name.lower(),
           model_name, model_name.lower(),
           model_name.lower(),

           model_name.lower(),model_name.lower(),
           model_name, model_name.lower(),
           model_name.lower(), model_name,
           model_name, model_name.lower(),
           model_name.lower(), model_name,
           model_name.lower(), model_name.lower(),
           model_name, model_name.lower(),
           model_name, model_name.lower(),
           model_name.lower(), model_name.lower(),
           model_name, model_name.lower(),
           model_name.lower(), model_name.lower(),
           model_name.lower(),
           )

    print("生成在【views.py】文件中的内容：")
    print(view_class)
    return view_class


#生成对应的html
def make_html(model_name):
    mubiao_html = """
{%% extends 'base.html' %%}
{%% block title %%}
    %s
{%% endblock %%}
{%% block action_url %%}
    {%% url 'andoriduilayer:%s_id' %s.id %%}
{%% endblock %%}
{%% block box_h1_title %%}
    添加数据
{%% endblock %%}
{%% block table_data %%}


{%% endblock %%}
{%% block box2_a %%}
    <a href='{{ django_server_yuming }}/andoriduilayer/%s/'>返回数据列表页</a>
{%% endblock %%}
    """  % (model_name.lower(), model_name.lower(),
            model_name.lower(), model_name.lower(),
            )
    print("生成在【%s.html】文件中的内容(不带table内容)：" % model_name)
    print(mubiao_html)
    return mubiao_html

#生成对应的formhtml
def make_form_html(model_name):
    mubiao_form_html = """
{%% extends 'andoriduilayercopy/%s.html' %%}
{%% block title %%}
    %sform
{%% endblock %%}
{%% block box_h1_title %%}
    添加数据出错页
{%% endblock %%}
{%% block table_data %%}


{%% endblock %%}
    """ % (model_name, model_name.lower())
    print("生成在【%sForm.html】文件中的内容(不带table内容)：" % model_name)
    print(mubiao_form_html)
    return mubiao_form_html




make_forms(model_name)
make_urls(model_name)
make_views(model_name)
make_html(model_name)
make_form_html(model_name)
