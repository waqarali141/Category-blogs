# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from forms import CategoryForm, PostForm
from models import Category, Post


class CategoryFormContext(object):
    def get_context_data(self, **kwargs):
        context = super(CategoryFormContext, self).get_context_data(**kwargs)
        category_form = CategoryForm()
        form_context = {'category': category_form}
        context.update(form_context)
        return context


class CategoryIndexView(LoginRequiredMixin, CategoryFormContext, ListView):
    template_name = 'blogs/category_index.html'
    context_object_name = 'Categories'

    def get_queryset(self):
        return Category.objects.all()


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    success_url = '/blogs'

    def form_valid(self, form):
        return super(CreateCategoryView, self).form_valid(form)


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    success_url = '/blogs'
    model = Category


class PostFormContext(object):
    def get_context_data(self, **kwargs):
        context = super(PostFormContext, self).get_context_data(**kwargs)
        post_form = PostForm()
        form_context = {'post_form': post_form}
        context.update(form_context)
        return context


class PostIndexView(LoginRequiredMixin, PostFormContext, DetailView):
    model = Category
    template_name = 'blogs/post_index.html'
    context_object_name = 'Category'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description']
    success_url = '/blogs'

    def form_valid(self, form):
        form.instance.category = Category.objects.get(pk=self.kwargs['pk'])
        form.instance.created_by = self.request.user
        form.instance.date_created = timezone.now()
        self.success_url = reverse('blog:PostIndex', args=(self.kwargs['pk'],))
        return super(CreatePostView, self).form_valid(form)
