
# 创建useragent的库
from fake_useragent import UserAgent
# 创建 动态的UserAgent
class UserAgentMiddleware(object):
    def process_request(self,request,spider):
        # request.headers.setdefault(b'User-Agent','abc')
        request.headers.setdefault(b'User-Agent',UserAgent().random)

# class ProxyMiddleware(object):
#     def process_request(self,request,spider):
#         #普通代理
#         # request.meta['proxy']='http://ip:port'
#         # # 独享代理
#         # request.meta['proxy']='http//user:passsword@ip:port'
#         request.meta['proxy']='http://47.105.91.226:8118'