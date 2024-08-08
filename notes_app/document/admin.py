from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'modified_at']
    search_fields = ['title', 'author', 'content']
    list_filter = ['author', 'modified_at']

    def content(self, obj):
        return obj.content

    content.short_description = 'Content'


#admin.site.register(Note)
