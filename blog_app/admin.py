from django.contrib import admin

from blog_app.models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'autor', 'created_at')
    search_fields = ('title', 'autor', 'content')
    prepopulated_fields = {'slug': ('title',)}
