import uuid

USER_KEY = 'uid'
TEN_YEARS = 60*60*24*365*10

class UserIDMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        #该参数是Django框架传递给中间件的响应处理函数。

    def __call__(self, request):
        uid = self.generate_uid(request)
        request.uid = uid
        #先生成了一个用于标记的uid，然后把uid存在request的字典里，键名也是uid
        response = self.get_response(request)
        #通过调用 self.get_response(request)，可以将请求传递给下一个处理程序，并获得其生成的响应
        response.set_cookie(USER_KEY,uid,max_age=TEN_YEARS,httponly=True)
        #uid 最终是存储在客户端的 cookie 中的
        return response

    def generate_uid(self,request):
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex
        return uid