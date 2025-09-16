class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def __call__(self, request: dict, *args, **kwargs):
        met = request.get('method', 'GET')
        if met == 'GET':
            return self.get(self.func, request, args, kwargs)
        else:
            return None

@HandlerGET
def contact(request):
    return 'Сергей Балакирев'

res = contact({'method': 'GET', 'url': 'contact.html'})
print(res)