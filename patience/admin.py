from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'pin_number', 'title', 'user', 'email'
    ]


admin.site.register(Blog, BlogAdmin)
