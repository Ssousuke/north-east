from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from backend.publication.models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    list_display_links = ('title', 'created_at', 'updated_at',)
    list_filter = ('title', 'created_at', 'updated_at',)


@admin.register(Category)
class CategogyAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_at', 'updated_at',)
    list_display_links = ('category', 'created_at', 'updated_at',)
    list_filter = ('category', 'created_at', 'updated_at',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'created_at', 'updated_at',)
    list_display_links = ('tag', 'created_at', 'updated_at',)
    list_filter = ('tag', 'created_at', 'updated_at',)
