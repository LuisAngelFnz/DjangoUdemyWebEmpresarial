from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['create', 'update']

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['create', 'update']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)