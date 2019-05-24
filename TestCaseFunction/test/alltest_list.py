from TestCaseFunction.autotest.Autotestchecksearch import TestSearchClass
from TestCaseFunction.autotest.test.agent.AutoTestLogin import TestLoginClass
from TestCaseFunction.autotest.test.agent.AutoTestAddMerchant import TestAddMerchantClass
from TestCaseFunction.autotest.test.agent.AutoTestAddCompanyMerchant import TestAddCompanyMerchantClass
from TestCaseFunction.autotest.test.agent.AutoTestAccountInfo import TestAccountInfoClass
from TestCaseFunction.autotest.test.agent.AutoTestCheckContract import TestCheckContractClass
from TestCaseFunction.autotest.test.agent.AutoTestDetails import TestDetailsClass
from TestCaseFunction.autotest.test.agent.AutoTestMerchantList import TestMerchantListClass
from TestCaseFunction.autotest.test.agent.AutoTestRevise import TestReviseClass
from TestCaseFunction.autotest.test.manager.AutoTestReview import TestReviewClass
from TestCaseFunction.autotest.test.agent.AutoTestMerchantListElementCheck import TestMerchantListClass
from TestCaseFunction.autotest.test.agent.AutoTestLogout import TestLogoutClass
from TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestCreateActivity import TestCreateActivityClass
from TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestEditActivity import TestEditActivityClass
from TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestHighLinesActivity import TestHighLinesActivityClass
from TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestDownLinesActivity import TestDownLinesActivityClass

def caselist():
    alltestnames = [
        # 'TestCaseFunction.autotest.test.agent.AutoTestLogin.TestLoginClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestAccountInfo.TestAccountInfoClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestCheckContract.TestCheckContractClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestDetails.TestDetailsClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestMerchantListElementCheck.TestMerchantListClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestMerchantList.TestMerchantListClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestAddMerchant.TestAddMerchantClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestAddCompanyMerchant.TestAddCompanyMerchantClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestRevise.TestReviseClass',
        # 'TestCaseFunction.autotest.test.manager.AutoTestReview.TestReviewClass',
        # 'TestCaseFunction.autotest.test.agent.AutoTestLogout.TestLogoutClass',
        'TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestCreateActivity.TestCreateActivityClass',
        'TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestEditActivity.TestEditActivityClass',
        'TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestHighLinesActivity.TestHighLinesActivityClass',
        'TestCaseFunction.autotest.test.marketing.rwhdgl.AutoTestDownLinesActivity.TestDownLinesActivityClass',







    ]
    print ('suite read case list success!! ')
    return alltestnames