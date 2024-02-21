from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Social

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    readonly_fields = ['create','update']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        
        return ['key','name']
        
