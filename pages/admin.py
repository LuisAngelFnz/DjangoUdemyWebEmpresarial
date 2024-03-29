from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['create', 'update']
    list_display = ('title','order')