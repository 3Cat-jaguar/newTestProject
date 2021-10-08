from django.contrib import admin
from .models import post_table, comment_table, user_table

@admin.register(post_table)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'image1',
        'image2',
        'image3',
        'content',
        'view_count',
        'created_at',
        'updated_at',
        'tag',
        'price',
        'user_key',
    )


@admin.register(comment_table)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'post_key',
        'content',
        'user_key',
        'created_at',
        'updated_at',
    )


@admin.register(user_table)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'password',
        'local',
    )