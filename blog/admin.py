from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['create', 'update']
    list_display    = ['name','create','update']

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['create', 'update']
    list_display    = ('title','autor','create','update','post_categories')
    ordering        = ('autor', 'date_publish')
    search_fields   = ('title', 'content', 'autor__username', 'categories__name')
    date_hierarchy  = 'date_publish'
    list_filter     = ('autor__username',)

    def post_categories(self, epost):
        return ','.join([e.name for e in epost.categories.all().order_by('name')])

    post_categories.short_description = 'Categorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)