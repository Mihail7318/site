from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# Register your models here.
from modeltranslation.admin import TranslationAdmin

from .models import *




class ChelensovetaInline(admin.TabularInline):
    fk_name = 'sovet'
    model = Chelensoveta
    extra = 1

@admin.register(Sovet)
class SovetAdmin(TranslationAdmin):
    inlines = [ChelensovetaInline]
    list_display = ('id', 'title',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_as = True
    save_on_top = True

