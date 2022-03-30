from django.contrib import admin
from .models import *


@admin.register(Tense)
class TenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'tense']
    list_display_links = ['id', 'tense']


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'translation', 'tense']
    list_display_links = ['id', 'text', 'translation']
    search_fields = ['text', 'translation']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_answers', 'right_answers', 'wrong_answers']


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'translation']
    list_display_links = ['id']
    search_fields = ['text', 'translation']
    list_editable = ['word', 'translation']