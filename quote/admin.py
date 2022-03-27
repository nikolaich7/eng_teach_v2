from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'translation']
    list_display_links = ['quote', 'translation']
    search_fields = ['quote', 'translation']