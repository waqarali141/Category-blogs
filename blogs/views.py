# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView

from forms import CategoryFormContext, PostFormContext, CommentFormContext, PostForm, CommentForm
from models import Category, Post, Comment, Like


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

    def get_success_url(self):
        return reverse('blog:PostIndex', args=(self.kwargs['Cid'],))

    def delete(self, request, *args, **kwargs):
        post_object = Post.objects.get(pk=kwargs['pk'])
        if request.user == post_object.created_by:
            return super(DeletePostView, self).delete(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorised', status=401)


class PostDetailView(LoginRequiredMixin, CommentFormContext, DetailView):
    model = Post
    template_name = 'blogs/Post_detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/edit_post.html'
    context_object_name = 'postform'

    def get_context_data(self, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        post = PostForm(instance=post)
        return {self.context_object_name: post,
                'category_id': self.kwargs['Cid'],
                'post_id': self.kwargs['pk']}

    def form_valid(self, form):
        if self.request.user == Post.objects.get(pk=self.kwargs['pk']).created_by:
            form = PostForm(self.request.POST, instance=Post.objects.get(pk=self.kwargs['pk']))
            self.object = form.save()
            self.success_url = reverse('blog:PostIndex', args=(self.kwargs['Cid'],))
            return super(PostUpdateView, self).form_valid(form)
        else:
            return HttpResponse('Unauthorised', status=401)


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


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'blogs/edit_comment.html'
    context_object_name = 'commentform'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        comment = Comment.objects.get(pk=self.kwargs['pk'])
        comment = CommentForm(instance=comment)
        return {self.context_object_name: comment,
                'category_id': self.kwargs['Cid'],
                'post_id': self.kwargs['Pid'],
                'comment_id': self.kwargs['pk']
                }

    def get_success_url(self):
        return reverse('blog:PostDetail', args=(self.kwargs['Cid'], self.kwargs['Pid']))

    def form_valid(self, form):
        if self.request.user == Comment.objects.get(pk=self.kwargs['pk']).user:
            form = CommentForm(self.request.POST, instance=Comment.objects.get(pk=self.kwargs['pk']))
            self.object = form.save()
            self.success_url = reverse('blog:PostDetail', args=(self.kwargs['Cid'], self.kwargs['Pid']))
            return super(CommentUpdateView, self).form_valid(form)
        else:
            return HttpResponse('Unauthorised', status=401)


def commentlikeview(request, CatId, Pid, CommentId):
    comment = Comment.objects.get(pk=CommentId)
    user = request.user
    like = Like()
    like.comment = comment
    like.user = user
    like.save()
    return HttpResponseRedirect(reverse('blog:PostDetail', args=(CatId, Pid,)))


def commentunlikeview(request, CatId, Pid, CommentId):
    comment = Comment.objects.get(pk=CommentId)
    user = request.user
    like = Like.objects.get(comment=comment, user=user)
    like.delete()
    return HttpResponseRedirect(reverse('blog:PostDetail', args=(CatId, Pid)))
