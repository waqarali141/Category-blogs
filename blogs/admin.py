# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blogs.models import Comment, Category, Like, Post

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Post)
