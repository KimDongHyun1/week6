from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'message']
    search_fields = ['author', 'message']