# def my_middleware(get_response):
#     print("one time initialization")
#     def my_function(request):
#         print("This is before view")
#         response = get_response(request)
#         print("this is after view")
#         return response
#     return my_function


class MyMiddleware:
    def _init_(self,get_response):
        self.get_response =   get_response
        print("one time initialization")

        def __call__(self,request):
            print("This is before view")
            response = self.get_response(request)
            print("This is after view")
            return response