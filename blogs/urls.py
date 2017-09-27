__author__ = 'waqarali'
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.CategoryIndexView.as_view(),
        name='CategoryIndex'),
    url(r'^login$', auth_views.login,
        name='login'),
    url(r'^post$', views.CreateCategoryView.as_view(),
        name='CategoryPost'),
    url(r'^post/delete/(?P<pk>[0-9 a-z A-Z]+)$', views.DeleteCategoryView.as_view(),
        name='DeleteCategory'),
    url(r'^post/(?P<pk>[0-9 a-z A-Z]+)$', views.PostIndexView.as_view(),
        name='PostIndex'),
    url(r'post/(?P<pk>[0-9 a-z A-Z]+)/add$', views.CreatePostView.as_view(),
        name='CreatePost')
]
