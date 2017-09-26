# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=35, verbose_name='Category Name')

    @property
    def get_posts(self):
        return self.relative_posts.all()


class Posts(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()

    category_belongs_to = models.ForeignKey(Categories, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    date_created = models.DateField()


class Comments(models.Model):
    comment = models.TextField()
    post_belongs_to = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)


class Likes(models.Model):
    count = models.IntegerField()
    comments_belongs_to = models.OneToOneField(Comments, on_delete=models.CASCADE, related_name='likes')




