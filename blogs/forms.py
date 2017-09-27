__author__ = 'waqarali'

from django.forms import ModelForm

from blogs.models import Category, Post, Comment


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CategoryFormContext(object):

    def get_context_data(self, **kwargs):
        context = super(CategoryFormContext, self).get_context_data(**kwargs)
        category_form = CategoryForm()
        form_context = {'category': category_form,
                        'user': self.request.user}
        context.update(form_context)
        return context


class PostFormContext(object):
    def get_context_data(self, **kwargs):
        context = super(PostFormContext, self).get_context_data(**kwargs)
        post_form = PostForm()
        form_context = {'post_form': post_form,
                        'user': self.request.user}
        context.update(form_context)
        return context


class CommentFormContext(object):
    def get_context_data(self, **kwargs):
        context = super(CommentFormContext, self).get_context_data(**kwargs)
        comment_form = CommentForm()
        form_context = {'comment_form': comment_form,
                        'user': self.request.user}
        context.update(form_context)
        return context
