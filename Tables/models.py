from django.db import models


class post_table(models.Model):
    TAGS = (
        (0, '소분'),
        (1, '나눔'),
        (2, '완료')
    )
    title = models.CharField(max_length=100, null=False)
    image1 = models.FileField(null=False)
    image2 = models.FileField(null=True)
    image3 = models.FileField(null=True)
    content = models.TextField(null=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.PositiveSmallIntegerField(choices=TAGS, null=False)
    price = models.PositiveIntegerField(default=0)
    user_key = models.PositiveIntegerField(null=False, default=0)


class comment_table(models.Model):
    post_key = models.PositiveIntegerField(null=False)
    content = models.TextField(null=False)
    user_key = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class user_table(models.Model):
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=16, null=False)
    local = models.PositiveIntegerField(null=False)

