# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from models import Category
from forms import CategoryForm


class CategoryFormContext(object):
    def get_context_data(self, **kwargs):
        context = super(CategoryFormContext, self).get_context_data(**kwargs)
        categoryform = CategoryForm()
        form_context = {'category': categoryform}
        context.update(form_context)
        return context


class CategoryIndexView(LoginRequiredMixin, CategoryFormContext, ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'Categories'

    def get_queryset(self):
        return Category.objects.all()


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = '/blogs'

    def form_valid(self, form):
        return super(CreateCategoryView, self).form_valid(form)
