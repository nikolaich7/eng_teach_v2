from django.contrib import admin
from .models import Tense, Example

@admin.register(Tense)
class TenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'tense']
    list_display_links = ['id', 'tense']

@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'translation', 'tense']
    list_display_links = ['id', 'text', 'translation']