from django.http import HttpResponse
from django.template.response import TemplateResponse


class ContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class TemplateRenderMixin:

    template_name = None

    def get_template_name(self):
        return self.template_name

    def render_to_response(self, request, context):
        return TemplateResponse(request, self.get_template_name(), context)


class CreateViewMixin:
    form_class = None

    def get_form_class(self):
        return self.form_class

    def get_form(self, form_data):
        return self.get_form_class()(form_data)

    def form_valid(self, form):
        # do it your sheet
        return HttpResponse(b'ok')

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_json())

