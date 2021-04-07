from django.contrib import admin
from django.urls import path

from myapp.views import CreateView, UserView, DeleteUserView

urlpatterns = [
    # path('django/', ResearchTemplateView.as_view()),
    # path('test2/', ShowMeCreate.as_view_new(name='myName'))
    path('fintest/', CreateView.as_view()),
    path('user/<int:user_id>/', UserView.as_view()),
    path('user-delete/<int:user_id>/', DeleteUserView.as_view()),
    ]
