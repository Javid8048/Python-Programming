import pdfkit

url = "https://emergingtalent.contentcontroller.com/ScormEngineInterface/dispatch/lti/ltiDispatch.html?studentId=600cf27a-fe98-41fc-8eb4-b420100a8412&studentName&redirectOnExitUrl=https%3A%2F%2Fawsrestart.instructure.com%2Fcourses%2F2826%2Fmodules&config=%7B%22dispatchVersion%22%3A%221%22%2C%22contentUrl%22%3A%22https%3A%2F%2Femergingtalent.contentcontroller.com%2Fapi%2Flaunch%2Fbundle%2Fcontent%2F32396%2FFgQEzI5bnHMAqDBxyQuF64asMEwx%3Fltirolesecret%3D%26learnerid%3DLEARNER_ID%26fname%3DLEARNER_FNAME%26lname%3DLEARNER_LNAME%26pipeurl%3DPIPE_URL%26redirecturl%3DREDIRECT_URL_REGISTRATION_ARGUMENT%22%2C%22dispatchRoot%22%3A%22https%3A%2F%2Femergingtalent.contentcontroller.com%2FScormEngineInterface%2Fdispatch%2F%22%2C%22preLaunchConfigurationUrl%22%3A%22https%3A%2F%2Femergingtalent.contentcontroller.com%2Fapi%2Flaunch%2Fconfig%2Fbundle%2Fcontent%2F32396%2FFgQEzI5bnHMAqDBxyQuF64asMEwx%22%7D&ltiOutcomeUrl=https%3A%2F%2Femergingtalent.contentcontroller.com%2FScormEngineInterface%2Fdispatch%2FDispatchRequest.jsp%3FmethodName%3DAssignmentandGradeServices%26tenant%3Dece7f9a0-2968-4539-8cd5-a96240ba1448%26ltiOutcomeInfo%3D42c16729-4790-4c6d-bc33-f84b2866eb3e%26score%3D_SCORE_%26ltiState%3D_STATE_"
pdfkit.from_url(url, 'output.pdf')