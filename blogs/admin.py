# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blogs.models import Comment, Category, Like, Post

admin.site.register(Comment)
admin.site.register(Like)


class AdminCategoryModel(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name',)
    list_filter = ('name',)


class AdminPostModer(admin.ModelAdmin):
    list_display = ('title', 'category.name', 'created_by')

admin.site.register(Category, AdminCategoryModel)
admin.site.register(Post, AdminPostModer)
