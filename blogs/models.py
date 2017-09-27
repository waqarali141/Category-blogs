# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """
        Model For Category
    """
    name = models.CharField(max_length=35, verbose_name='Category Name')

    # Return all the related posts of the given category
    @property
    def get_posts(self):
        return self.posts.all().order_by('-date_created')


class Post(models.Model):
    """
        Model For Post
    """
    title = models.CharField(max_length=35)
    description = models.TextField()

    # Which category post belongs to
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)

    # The User who created the Post
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')

    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField()

    # Return All the comments for the given Post
    @property
    def get_comments(self):
        return self.comments.all().order_by('-dated')


class Comment(models.Model):
    """
        Model For Comment
    """
    text = models.TextField(verbose_name= 'Comment Text')

    # Which post comment belongs to
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    dated = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

    # Which user has commented this
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Like(models.Model):
    """
        Model For Like
    """
    # Comment this like belongs to
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')

    # user who liked the comment
    user = models.OneToOneField(User, on_delete=models.CASCADE)
