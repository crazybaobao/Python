# 创建test.py文件
def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"Hello World"]

# import dns.resolver
#
# iplist = []
# appdomain = "www.baidu.com"
#
#
# def get_iplist(domain=""):
#     try:
#         A = dns.resolver.query(domain, 'A')
#     except Exception as e:
#         print("dns resolver error:" + str(e))
#         return
#     for i in A.response.answer:
#         for j in i.items:
#             if j.rdtype == 1:
#                 iplist.append(j.address)
#     return True
#
#
# get_iplist(appdomain)
# print(iplist)
