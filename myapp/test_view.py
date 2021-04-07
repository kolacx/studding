from django.http import HttpResponseNotAllowed


class ViewNew:

    http_methods = ['get', 'post']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def as_view_new(cls, **initkwargs):

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            self.setup(request, *args, **kwargs)
            return self.dispatch(request, *args, **kwargs)

        return view

    def setup(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_methods:
            handler = getattr(self, request.method.lower(), HttpResponseNotAllowed)
        else:
            handler = HttpResponseNotAllowed
        return handler(request, *args, **kwargs)