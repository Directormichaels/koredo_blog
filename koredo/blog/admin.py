from django.contrib import admin
from .models import Post, Category, Comment


admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ['title', 'slug', 'author', 'publish', 'status']
 list_filter = ['status', 'created', 'publish', 'author']
 search_fields = ['title', 'body']
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ['author']
 date_hierarchy = 'publish'
 ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
        
admin.site.register(Comment, CommentAdmin)