
import json


def responseheaders(flow):
    flow.response.headers['Cache-Control'] = 'no-cachewewfwe'
    flow.response.headers['Pragma'] = 'no-cacheewwew33'
    print(flow.response.headers['content-length'],'-------------------------------')



def response(flow):
#     '''
#     HTTPEvent 下面所有事件参数都是 flow 类型 HTTPFlow
#     可以在API下面查到 HTTPFlow, 下面有一个属性response 类型 TTPResponse
#     HTTPResponse 有个属性为 content 就是response在内容,更多属性可以查看 文档
#     :param flow: 
#     :return: 
#     '''

#     if flowfilter.match(self.filter, flow):
#         #匹配上后证明抓到的是问题了, 查答案
    flow.response.content = b"<script>alert('mytest')</script>"
#         #获取问题
#         question = quiz['quiz']
#         print(question)

#         #获取答案
#         answer = self.answer_set.find_one({"quiz":question})
#         if answer is None:
#             print('no answer')
#         else:
#             answerIndex = int(answer['answer'])-1
#             options = answer['options']
#             print(options[answerIndex])

    #这里简单演示下start事件
def start():
    return TNWZ()

