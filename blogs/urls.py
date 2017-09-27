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

    url(r'^logout$', auth_views.logout,
        name='logout'),

    url(r'^category/add$', views.CreateCategoryView.as_view(),
        name='CategoryPost'),

    url(r'^category/delete/(?P<pk>[0-9 a-z A-Z]+)$', views.DeleteCategoryView.as_view(),
        name='DeleteCategory'),

    url(r'^category/(?P<pk>[0-9 a-z A-Z]+)$', views.CategoryDetailView.as_view(),
        name='PostIndex'),

    url(r'category/(?P<pk>[0-9 a-z A-Z]+)/post/add$', views.CreatePostView.as_view(),
        name='CreatePost'),

    url(r'category/(?P<Cid>[0-9 a-z A-Z]+)/post/delete/(?P<pk>[0-9 a-z A-Z]+)>', views.DeletePostView.as_view(),
        name='DeletePost'),

    url(r'category/(?P<Cid>[0-9 a-z A-Z]+)/post/(?P<pk>[0-9 a-z A-Z]+)$', views.PostDetailView.as_view(),
        name='PostDetail'),

    url(r'category/(?P<Cid>[0-9 a-z A-Z]+)/post/(?P<pk>[0-9 a-z A-Z]+)/add/comment$', views.CreateCommentView.as_view(),
        name='CreateComment'),

    url(r'category/(?P<Cid>[0-9 a-z A-Z]+)/post/(?P<Pid>[0-9 a-z A-Z]+)/delete/comment/(?P<pk>[0-9 a-z A-Z]+)$', views.DeleteCommentView.as_view(),
    name='DeleteComment'),

    url(r'category/(?P<Cid>[0-9 a-z A-Z]+)/post/(?P<pk>[0-9 a-z A-Z]+)/update$', views.PostUpdateView.as_view(),
        name='UpdatePostView'),

    url(r'category/(?P<Cid>[0-9 a-z A-Z]+)/post/(?P<pk>[0-9 a-z A-Z]+)/update/save$', views.PostUpdate.as_view(),
        name='UpdatePost')

]
