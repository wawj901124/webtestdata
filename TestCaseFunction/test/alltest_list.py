from TestCaseFunction.autotest.Autotestchecksearch import TestSearchClass
from TestCaseFunction.autotest.test.agent.AutoTestLogin import TestLoginClass
from TestCaseFunction.autotest.test.agent.AutoTestAddMerchant import TestAddMerchantClass
from TestCaseFunction.autotest.test.agent.AutoTestAddCompanyMerchant import TestAddCompanyMerchantClass

def caselist():
    alltestnames = [
    # 'TestCaseFunction.autotest.test.agent.AutoTestLogin.TestLoginClass',
        'TestCaseFunction.autotest.test.agent.AutoTestAddMerchant.TestAddMerchantClass',
        'TestCaseFunction.autotest.test.agent.AutoTestAddCompanyMerchant.TestAddCompanyMerchantClass',

    ]
    print ('suite read case list success!! ')
    return alltestnames