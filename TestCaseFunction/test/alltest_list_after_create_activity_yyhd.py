from TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestEditActivity import TestEditActivityClass
from TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestEditTicket import TestEditTicketClass
from TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestHighLinesActivity import TestHighLinesActivityClass
from TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestEditProcessingActivity import TestEditProcessingActivityClass
from TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestDownLinesActivity import TestDownLinesActivityClass
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

        'TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestEditActivity.TestEditActivityClass',
        'TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestEditTicket.TestEditTicketClass',
        'TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestHighLinesActivity.TestHighLinesActivityClass',
        'TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestEditProcessingActivity.TestEditProcessingActivityClass',
        'TestCaseFunction.autotest.test.marketing.yyhdgl.AutoTestDownLinesActivity.TestDownLinesActivityClass'

    ]
    print ('suite read case list success!! ')
    return alltestnames