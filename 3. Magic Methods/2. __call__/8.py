class HandlerGET:
    def __init__(self, methods = ('GET', )):
        self.methods = methods

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            met = request.get('method', 'GET')
            if met in self.methods:
                if met == 'GET':
                    return self.get(func, request, args, kwargs)
                if met == 'POST':
                    return self.post(func, request, args, kwargs)
            return None
        return wrapper





@HandlerGET(methods = ('GET', 'POST'))
def contact(request):
    return 'Сергей Балакирев'

res = contact({'method': 'POST', 'url': 'contact.html'})
print(res)