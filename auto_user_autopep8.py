# 找出跟目录下所有py文件
# pip install autopep8
# 默认情况下，autopep8只修复空格问题。所以，默认情况下，autopep8不会修复 E711 和 E712 ，也不会修复弃用的代码 W6。
# 为了应用这些更加 aggressive 的修复，使用 --aggressive 选项：
# autopep8 --in-place --aggressive --aggressive D:\pycharmproject\webtestdata\actualtool\修复练习\修复2\models.py
import os


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                L.append(os.path.join(root, file))
    print(L)
    print(len(L))
    return L

# 使用cmd命令挨个执行替换所有文件


def runcmd(dir_list):
    num = 1
    for one in dir_list:
        print("处理第%s个文件" % str(num))
        order = "workon myfirst"
        result = os.popen(order)
        f = result.read()

        order = "autopep8 --in-place --aggressive --aggressive %s" % str(one)
        result = os.popen(order)
        f = result.read()
        print(f)
        print("处理文件：[%s]" % str(one))
        num = num + 1


file_dir = r'D:\debugpycharmproject\debugwebtestdata'
dir_list = file_name(file_dir)
runcmd(dir_list)
