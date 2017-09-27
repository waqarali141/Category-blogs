# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView

from forms import CategoryFormContext, PostFormContext, CommentFormContext, PostForm
from models import Category, Post, Comment


class CategoryIndexView(LoginRequiredMixin, CategoryFormContext, ListView):
    template_name = 'blogs/category_index.html'
    context_object_name = 'Categories'

    def get_queryset(self):
        return Category.objects.all()


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    success_url = '/blogs'
    fields = ['name']

    def form_valid(self, form):
        return super(CreateCategoryView, self).form_valid(form)


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    success_url = '/blogs'
    model = Category


class CategoryDetailView(LoginRequiredMixin, PostFormContext, DetailView):
    model = Category
    template_name = 'blogs/category_detail.html'
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


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    # success_url = reverse('blog:PostIndex', args=(self.kwargs['pk'],))

    def get_success_url(self):
        return reverse('blog:PostIndex', args=(self.kwargs['Cid'],))


class PostDetailView(LoginRequiredMixin, CommentFormContext, DetailView):
    model = Post
    template_name = 'blogs/Post_detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogs/edit_post.html'
    context_object_name = 'postform'

    def get_context_data(self, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        post = PostForm(instance=post)
        return {self.context_object_name: post,
                'category_id': self.kwargs['Cid'],
                'post_id': self.kwargs['pk']}


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'description']

    def form_valid(self, form):
        form = PostForm(self.request.POST, instance=Post.objects.get(pk=self.kwargs['pk']))
        self.object = form.save()
        self.success_url = reverse('blog:PostIndex', args=(self.kwargs['Cid'],))
        return super(PostUpdate, self).form_valid(form)


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.dated = timezone.now()
        self.success_url = reverse('blog:PostDetail', args=(self.kwargs['Cid'], self.kwargs['pk'],))
        return super(CreateCommentView, self).form_valid(form)


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('blog:PostDetail', args=(self.kwargs['Cid'], self.kwargs['Pid'],))
