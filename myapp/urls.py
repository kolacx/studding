from django.contrib import admin
from django.urls import path

from myapp.views import CreateView

urlpatterns = [
    # path('django/', ResearchTemplateView.as_view()),
    # path('test2/', ShowMeCreate.as_view_new(name='myName'))
    path('fintest/', CreateView.as_view())
    ]
