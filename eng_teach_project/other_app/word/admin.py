from django.contrib import admin
from .models import Word

@admin.register(Word)
class Word_enAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'translation', 'lvl_know']
    list_display_links = ['id']
    list_editable = ['word', 'translation', 'lvl_know']
    list_filter = ['lvl_know']
    search_fields = ['word', 'translation']
    list_per_page = 5