class RenderDigit:
    def __call__(self, s: str, *args, **kwargs):
        if s.isdigit():
            return int(s)
        else:
            return None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper():
            return list(map(self.render, func().split()))
        return wrapper

render = RenderDigit()
input_dg = InputValues(render)(input)

res = input_dg()
print(res)