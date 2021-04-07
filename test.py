class Foo:
    attr_first = False

    def __init__(self):
        self.attr_second = True

a = Foo()
print(a.attr_first)             # loockup class
print(a.attr_second)            # Loockup instance

print(Foo.attr_first)           # Loockup class
# print(Foo.attr_second)        # Loockup class. Dont see becouse attr_seccond life in instance
print(dir(a)[::-1])
print(dir(Foo)[::-1])

a.attr_first = False            # Lockup to instance and make variable attr_first = False
print(a.attr_first)             # print value of new instance variable

Foo.attr_third = 'Third'        # Make new variable to class
print(Foo.attr_third)

print(dir(a)[::-1])
print(dir(Foo)[::-1])























from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView as DjangoTemplateView
from django.views.generic import View

from django import forms

from myapp.test_view import ViewNew


class ShowMeGetView(ViewNew):

    template_name = None

    def get(self, request, *args, **kwargs):
        print(dir(self))
        print(getattr(self, 'name'))
        context = self.get_context()
        return TemplateResponse(request, self.template_name, context)

    def get_context(self):
        return {}


class ShowMePostView(ViewNew):

    form_class = None

    def post(self, request, *args, **kwargs):

        if self.valid_post(request):
            return HttpResponse(b'All Good')
        else:
            return HttpResponse(b'STFUP and doit')

    def valid_post(self, request):
        return self.form_class(request.POST).is_valid()


class ShowMeDeleteView(ViewNew):

    def delete(self, request, *args, **kwargs):

        return HttpResponse(b'delete')


class FormForPost(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)


class ShowMeCreate(ShowMeGetView, ShowMePostView):

    template_name = 'index.html'
    form_class = FormForPost

    def get_context(self):
        return {'user1': 'Sanya', 'user2': 'kolya'}
















class ResearchTemplateView(DjangoTemplateView):
    template_name = 'index.html'


class TemplateView(View):

    template_name = None
    context = None

    def get(self, request, *args, **kwargs):
        if self.context is not None:
            self.context.update({'request': request})

        return TemplateResponse(request, self.template_name, context=self.context)


class TestTemplateView(TemplateView):
    template_name = 'index.html'








