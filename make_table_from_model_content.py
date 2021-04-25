# 根据modelcontent.txt中的内容生成一个html中的table
class MakeTable:

    def __init__(self, modelcontentfile, modelname):
        self.model_content_file = modelcontentfile
        self.model_name = modelname
        self.all_xiang_list = self.get_model_content()

    def get_model_content(self):
        f = open(self.model_content_file, "r", encoding="utf8")  # 打开文件

        model_name = self.model_name

        all_xiang_list = []

        for i in f:  # 遍历查看每一行的内容
            one_list = []
            # 获取模块名小写
            one_list.append(model_name.lower())

            # 获取table的标签名
            lie_list = i.split("verbose_name")  # 以等号分割
            # print(lie_list)
            label_name_yu = lie_list[1].strip()
            # print("label_name:")
            # print(label_name)
            label_name_yu_list = label_name_yu.split('"')
            label_name = label_name_yu_list[1]
            # print("label_name:")
            # print(label_name)
            one_list.append(label_name)

            # 获取html元素tag类型:input、select等
            lie_list = i.split("models.")  # 以等号分割
            # print(lie_list)
            tag_name_yu_list = lie_list[1].split("(")
            # print(tag_name_yu_list)
            tag_html_type = tag_name_yu_list[0]
            # print("tag_html_type:")
            # print(tag_html_type)
            one_list.append(tag_html_type)

            # 获取tag的id和name的值
            lie_list = i.split("=")  # 以等号分割
            # print(lie_list)
            tag_id = lie_list[0].strip()
            # print("tag_id:")
            # print(tag_id)
            one_list.append(tag_id)

            # 获取html元素tag类型:input、select等,外键类型 self或者模块名
            lie_list = i.split("models.")  # 以等号分割
            # print(lie_list)
            tag_name_yu_list = lie_list[1].split("(")
            waijian_type_yu_list = tag_name_yu_list[1].split(",")
            # print(waijian_type_yu_list)
            waijian_type = waijian_type_yu_list[0].strip().lower()
            # print(waijian_type)
            one_list.append(waijian_type)

            print(one_list)
            all_xiang_list.append(one_list)

        print(all_xiang_list)
        return all_xiang_list

    #生成table
    def make_table(self):
        all_xiang_list = self.all_xiang_list
        table_zong = ""

        # 根据列表数据生成table内容
        table_start_content = """    <table cellpadding="0" cellspacing="0">"""

        table_zong = table_zong + table_start_content + '\n'

        # 根据列表生成内容
        for one_list in all_xiang_list:
            model_name = one_list[0]
            label_name = one_list[1]
            tag_html_type = one_list[2]
            tag_id = one_list[3]
            waijian_type = one_list[4]
            if tag_html_type == "CharField" or tag_html_type == "IntegerField":
                table_one_tr = """        <tr>
                    <td>
                        <label>%s:</label>
                    </td>
                    <td>
                        <input id="%s" name="%s" type="text" value="{{ %s.%s }}"/>
                    </td>
                </tr>""" % (label_name, tag_id, tag_id, model_name, tag_id)

            elif tag_html_type == "BooleanField":
                table_one_tr = """        <tr>
                    <td>
                        <label>%s:</label>
                    </td>
                    <td>
                        <input type="radio" id="%s" name="%s"  value=1 {%% if %s.%s == 1 %%} checked="checked"{%% endif %%}>是
                        <input type="radio" id="%s" name="%s"  value=0 {%% if %s.%s == 0 %%} checked="checked"{%% endif %%}>否
                    </td>
                </tr>""" % (label_name, tag_id, tag_id, model_name, tag_id, tag_id, tag_id, model_name, tag_id)

            elif tag_html_type == "ForeignKey":
                if str(waijian_type) == "'self'":
                    table_one_tr = """        <tr>
                        <td>
                            <label>%s:</label>
                        </td>
                        <td>
                            <select id="%s" name="%s">
                                <option value=""
                                        {%% if %s.%s_id == None %%}
                                            selected="selected"
                                        {%% endif %%}>
                                        ---请选择
                                </option>
                                {%% for cab in %s_all %%}
                                    <option
                                            value={{ cab.id }}
                                                    {%% if cab.id == %s.%s_id %%}
                                                        selected="selected"
                                                    {%% endif %%}>
                                        [{{ cab.test_project }}]-[{{ cab.test_module }}]-[{{ cab.test_page }}]_[{{cab.test_case_title }}]
                                    </option>
                                {%% endfor %%}

                            </select>

                        </td>""" % (label_name, tag_id, tag_id, model_name, tag_id, model_name, model_name, tag_id)
                else:
                    table_one_tr = """        <tr>
                        <td>
                            <label>%s:</label>
                        </td>
                        <td>
                            <select id="%s" name="%s">
                                <option value=""
                                        {%% if %s.%s_id == None %%}
                                            selected="selected"
                                        {%% endif %%}>
                                        ---请选择
                                </option>
                                {%% for cab in %s_all %%}
                                    <option
                                            value={{ cab.id }}
                                                    {%% if cab.id == %s.%s_id %%}
                                                        selected="selected"
                                                    {%% endif %%}>
                                        [{{ cab.test_project }}]-[{{ cab.test_module }}]-[{{ cab.test_page }}]_[{{cab.test_case_title }}]
                                    </option>
                                {%% endfor %%}

                            </select>

                        </td>""" % (label_name, tag_id, tag_id, model_name, tag_id, tag_id, model_name, tag_id)



            else:
                table_one_tr = ""

            table_zong = table_zong + table_one_tr + "\n"

        # 最后内容
        table_end_content = """    </table>"""

        table_zong = table_zong + table_end_content

        print("table_zong:")
        print(table_zong)
        return table_zong

    #生成table form
    def make_table_form(self):
        all_xiang_list = self.all_xiang_list

        table_zong = ""

        # 根据列表数据生成table内容
        table_start_content = """    <table cellpadding="0" cellspacing="0">"""

        table_zong = table_zong + table_start_content + '\n'

        # 根据列表生成内容
        for one_list in all_xiang_list:
            model_name = one_list[0]
            label_name = one_list[1]
            tag_html_type = one_list[2]
            tag_id = one_list[3]
            waijian_type = one_list[4]
            if tag_html_type == "CharField" or tag_html_type == "IntegerField":
                table_one_tr = """        <tr>
                    <td>
                        <label>%s:</label>
                    </td>
                    <td>
                        <input id="%s" name="%s" type="text" value="{{ %sform.%s.value }}"/>
                    </td>
                </tr>""" % (label_name, tag_id, tag_id, model_name, tag_id)

            elif tag_html_type == "BooleanField":
                table_one_tr = """        <tr>
                    <td>
                        <label>%s:</label>
                    </td>
                    <td>
                        <input type="radio" id="%s" name="%s"  value=1 {%% if %sform.%s.value == 1 %%} checked="checked"{%% endif %%}>是
                        <input type="radio" id="%s" name="%s"  value=0 {%% if %sform.%s.value == 0 %%} checked="checked"{%% endif %%}>否
                    </td>
                </tr>""" % (label_name, tag_id, tag_id, model_name, tag_id, tag_id, tag_id, model_name, tag_id)

            elif tag_html_type == "ForeignKey":
                print("外键类型：")
                print(waijian_type)
                if str(waijian_type) == "'self'":
                    table_one_tr = """        <tr>
                        <td>
                            <label>%s:</label>
                        </td>
                        <td>
                            <select id="%s" name="%s">
                                <option value=""
                                        {%% if %s.%s_id == None %%}
                                            selected="selected"
                                        {%% endif %%}>
                                        ---请选择
                                </option>
                                {%% for cab in %s_all %%}
                                    <option
                                            value={{ cab.id }}
                                                    {%% if cab.id == %s.%s_id %%}
                                                        selected="selected"
                                                    {%% endif %%}>
                                        [{{ cab.test_project }}]-[{{ cab.test_module }}]-[{{ cab.test_page }}]_[{{cab.test_case_title }}]
                                    </option>
                                {%% endfor %%}

                            </select>

                        </td>""" % (label_name, tag_id, tag_id, model_name, tag_id, model_name, model_name, tag_id)

                else:
                    table_one_tr = """        <tr>
                        <td>
                            <label>%s:</label>
                        </td>
                        <td>
                            <select id="%s" name="%s">
                                <option value=""
                                        {%% if %s.%s_id == None %%}
                                            selected="selected"
                                        {%% endif %%}>
                                        ---请选择
                                </option>
                                {%% for cab in %s_all %%}
                                    <option
                                            value={{ cab.id }}
                                                    {%% if cab.id == %s.%s_id %%}
                                                        selected="selected"
                                                    {%% endif %%}>
                                        [{{ cab.test_project }}]-[{{ cab.test_module }}]-[{{ cab.test_page }}]_[{{cab.test_case_title }}]
                                    </option>
                                {%% endfor %%}

                            </select>

                        </td>""" % (label_name, tag_id, tag_id, model_name, tag_id, tag_id, model_name, tag_id)

            else:
                table_one_tr = ""

            table_zong = table_zong + table_one_tr + "\n"

        # 最后内容
        table_end_content = """    </table>"""

        table_zong = table_zong + table_end_content

        print("table_zong:")
        print(table_zong)

    #生产在xadmin中的内容
    def make_xadmin(self):
        all_xiang_list = self.all_xiang_list

        aiduan_list = []
        # 根据列表生成内容
        for one_list in all_xiang_list:
            tag_id = one_list[3]
            aiduan_list.append(tag_id)

        mubiao = """
from .models import %s


#%sadmin
class %sXAdmin(object):
    ziduan = %s
    

    list_display = %s  # 定义显示的字段
    search_fields = ['%s', ]  # 定义搜索字段
    list_filter = ['%s', ]  # 定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    readonly_fields = ['add_time', ]
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  #
    # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    list_display_links = ['%s', ]  # 设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['%s', ]  # 显示数据详情

    # 批量设置选中用例为 not run

    def patch_set_not_run(self, request, querset):
        for qs_one in querset:
            # 再删除本体
            qs_one.is_run_case = '0'
            qs_one.save()

    # 批量设置选中用例为 not run
    def patch_set_run(self, request, querset):
        for qs_one in querset:
            # 再删除本体
            qs_one.is_run_case = '1'
            qs_one.save()

    patch_set_not_run.short_description = "批量设置用例为不运行"
    patch_set_run.short_description = "批量设置用例为运行"

    actions = [patch_set_not_run, patch_set_run, ]


# 在xadmin中注册%s
xadmin.site.register(%s, %sXAdmin)
    """ % (self.model_name, self.model_name,
           self.model_name, str(aiduan_list),
           str(aiduan_list), str(aiduan_list[0]),
           str(aiduan_list[0]), str(aiduan_list[0]),
           str(aiduan_list[0]), self.model_name,
           self.model_name, self.model_name
           )

        print("在xadmin文件中的内容：")
        print(mubiao)



if __name__ == "__main__":
    modelcontentfile = "modelcontent.txt"
    modelname = "CheckTestCase"
    mt = MakeTable(modelcontentfile=modelcontentfile, modelname=modelname)
    # mt.make_table()
    # mt.make_table_form()
    mt.make_xadmin()
