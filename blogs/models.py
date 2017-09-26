# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=35, verbose_name='Category Name')

    @property
    def get_posts(self):
        return self.relative_posts.all()


class Post(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    date_created = models.DateField()


class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)


class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.OneToOneField(User, on_delete=models.CASCADE)





