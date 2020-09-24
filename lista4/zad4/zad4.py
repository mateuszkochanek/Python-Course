from inspect import getfullargspec

registry = {}
class OverloadedFunction(object):
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *args, **kwargs):
        function = registry.get(self.get_key(args=args))
        if function is None:
            raise TypeError("no match")
        return function(*args, **kwargs)
    def register(self):
        registry[self.get_key()] = self.fn
    def get_key(self,args=None):
        if args is None:
            args = getfullargspec(self.fn).args
        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
            ])

def overload(fn):
    func = OverloadedFunction(fn)
    func.register()
    return func

@overload
def functest(a):
    print("funkcja z jednym argumentem:",a)

@overload
def functest(a,b):
    print("funkcja z dwoma argumentami:",a,b)

@overload
def functest(a,b,c):
    print("funkcja z trzema argumentami:",a,b,c)


functest(1,2,3)
functest(1,2)
functest(1,2,3)
functest(3)