from django.http import HttpResponse
from django.template.response import TemplateResponse
from django import forms

from myapp.view_new import ViewsSuper


class TemplateViewMethods(ViewsSuper):

    template_name = None

    def get(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        return TemplateResponse(request, self.template_name, context)

    def get_context(self, request, *args, **kwargs):
        return {}


class CreateViewMethods(ViewsSuper):

    form_class = None

    def post(self, request, *args, **kwargs):
        if self.valid_post(request, *args,**kwargs):
            # In this place we add to DB
            return HttpResponse(b'post ok')
        else:
            # In this place we Response some error

            return HttpResponse(f'not ok {self.form_class(request.POST).errors.as_json()}')

    def valid_post(self, request, *args, **kwargs):
        return self.form_class(request.POST).is_valid()


class FormSuper(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)


class CreateView(CreateViewMethods, TemplateViewMethods):

    template_name = 'index.html'
    form_class = FormSuper
