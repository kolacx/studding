from django.http import HttpResponse
from django.template.response import TemplateResponse
from django import forms

from myapp.view_new import ViewsSuper
from myapp.mixin import TemplateRenderMixin, ContextMixin, CreateViewMixin

from myapp.models import User


class TemplateViewMethods(TemplateRenderMixin, ContextMixin, ViewsSuper):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(request, context)


class CreateViewMethods(CreateViewMixin, TemplateRenderMixin, ContextMixin, ViewsSuper):

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        form = self.get_form(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(request, context)


class FormSuper(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)


class CreateView(CreateViewMethods, TemplateViewMethods):
    template_name = 'index.html'
    form_class = FormSuper

    def form_valid(self, form):
        User.objects.create(name=form.data['name'],
                            age=form.data['age'])
        return super().form_valid(form)

    def form_invalid(self, form):
        print('Enter Invalid')
        return super().form_invalid(form)


class TemplateView(TemplateViewMethods):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {'user': ['qwe1', 'qwe2'], 'user2': 'qqwwee'}
        return context


class UserView(TemplateViewMethods):
    template_name = 'user.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        context = {'users': user}

        return self.render_to_response(request, context)


class DeleteUserView(TemplateViewMethods):
    template_name = 'user.html'

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        user.delete()
        return self.render_to_response(request, context=None)
