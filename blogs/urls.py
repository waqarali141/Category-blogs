__author__ = 'waqarali'
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.CategoryIndexView.as_view(), name='CategoryIndex'),
    url(r'^login$', auth_views.login, name='login'),
    url(r'^post$', views.CreateCategoryView.as_view(), name='CategoryPost')
]
