import requests,json
from APIAutoTest.util.md5sign import  IIATF_sign_verify
from APIAutoTest.util.my_log import MyLog

class BaseFrame(object):
    
    def outPutMyLog(self,context):
        mylog = MyLog(context)
        mylog.runMyLog()

    def outPutErrorMyLog(self,context):
        mylog = MyLog(context)
        mylog.runErrorLog()

    # 获取sign值
    def get_sign_data(self,data,private_rsa_key):
        signdata = IIATF_sign_verify.rsa_MD5sign(data,private_rsa_key)
        self.outPutMyLog("b_sign_data:%s" % signdata)
        #签名后的数据转换为str类型数据
        s_sign_data = str(signdata, encoding='utf-8')
        self.outPutMyLog("s_sign_data:%s" % s_sign_data)
        return s_sign_data

    #字节类型数据转转为字符串类型数据
    def byte_to_string(self,b_data):
        s_data = str(b_data, encoding='utf-8')
        self.outPutMyLog("s_data:%s" % s_data)
        return s_data

    #字符串类型数据转换为字节类型
    def string_to_byte(self,s_data):
        self.outPutMyLog(type(s_data))
        if  not str(s_data) ==  "<class 'str'>":
            self.outPutErrorMyLog("传入的数据的的数据类型非字符串类型，为：.%s"% type(s_data))
            s_data = str(s_data) #将传入值修改为string类型
            self.outPutErrorMyLog("已经将传入的数据转换为字符串类型")
        s_data_m = s_data.replace(" ", "")  # 去掉字符串中间的空格
        s_data_m = s_data_m.replace("'", '"')  # 单引号变为双引号
        b_data = bytes(s_data_m, encoding='utf-8')
        self.outPutMyLog("b_data:%s" % b_data)
        return b_data

    #post json请求
    def post_json(self,url,json_data):
        response = requests.post(url,json=json_data)
        response_text = response.text
        self.outPutMyLog("响应的test信息为：%s" % response_text)
        return response_text

    #post data请求
    def post_data(self,url,json_data):
        #json字典类型数据转换为字符串类型
        body = json.dumps(json_data)
        response=requests.post(url=url,data=body)
        response_text = response.text
        self.outPutMyLog("响应的test信息为：%s" % response_text)
        return response_text

    #post data请求
    def post_rdata(self,url,rdata):
        response=requests.post(url=url,data=rdata)
        response_text = response.text
        self.outPutMyLog("响应的test信息为：%s" % response_text)
        return response_text

    # 获取dict key 中的value 的方法
    def get_value(self,dict_data, dict_key):
        data_type = type(dict_data)
        self.outPutMyLog(data_type)
        self.outPutMyLog(str(data_type))
        if str(data_type) ==  "<class 'dict'>":
            dict_value = dict_data[dict_key]
            self.outPutMyLog("获取键值对成功.传入的数据%s是字典类型数据,获得的键【%s】的值为：%s."% (dict_data,dict_key,dict_value))
            return dict_value
        else:
            self.outPutErrorMyLog("获取键值对失败.传入的数据%s非字典类型数据，类型为：%s."% (dict_data,type(dict_data)))
            return dict_data


        # self.outPutMyLog("find:%s" % find)
        # # self.outPutMyLog(find)
        # data = json.loads(find)
        # self.outPutMyLog(data)
        # self.outPutMyLog(type(data))
        # ss = data['data']
        # s1 = eval(ss)
        # activity_id = s1["coupons"][number]["activity_id"]
        # seq = s1["coupons"][number]["seq"]
        # if value == "activity_id":
        #     self.outPutMyLog("activity_id:%s" % activity_id)
        #     return activity_id
        #
        # else:
        #     return seq

if __name__ == '__main__':
    json_data = {"mer": 10000,
                 "data": '{}',
                 "sign": '1234',
                 }
    baseframe = BaseFrame()
    baseframe.get_value(json_data,"mer")
    data = {"activity_id": "123", "seq": "123"}
    b_data = baseframe.string_to_byte(data)




