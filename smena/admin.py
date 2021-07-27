from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import *



@admin.register(Smena)
class SmenaAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'rubric', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status', 'rubric',)
    save_as = True
    save_on_top = True

