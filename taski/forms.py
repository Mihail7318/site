from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, SelectMultiple, CheckboxInput
from .models import *


class ReataskiForm(forms.ModelForm):
    class Meta:
        model = Zadacha
        fields = [ 'title_en', 'title_ru', 'slug', 'yved', 'content_ru', 'content_en', 'rubric', 'image', 'status']

        widgets = {
            "status": Select(attrs={'class': 'form-control', 'placeholder': 'Статус задачи'}),
            "yved": CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Уведомить'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи'}),
            "title_ru": TextInput(attrs={'class': 'form-control', 'id': 'title_ru', 'placeholder': 'Название задачи [ru]'}),
            "title_en": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи [en]'}),
            "slug": TextInput(attrs={'class': 'form-control', 'id': 'slug', 'placeholder': 'ссылка'}),
            "content": forms.CharField(widget=CKEditorWidget()),
            "content_ru": forms.CharField(widget=CKEditorWidget()),
            "content_en": forms.CharField(widget=CKEditorWidget()),
            "rubric": Select(attrs={'class': 'form-control', 'placeholder': 'Категория задачи'}),
            "image": FileInput(attrs={'class': 'form-control', 'placeholder': 'Изображение задачи'}),
        }

class TaskiForm(forms.ModelForm):
    class Meta:
        model = Zadacha
        fields = [ 'title_en', 'title_ru', 'slug', 'yved', 'content_ru', 'content_en', 'rubric', 'image', 'status']

        widgets = {
            "status": Select(attrs={'class': 'form-control', 'placeholder': 'Статус задачи'}),
            "yved": CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Уведомить'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи'}),
            "title_ru": TextInput(attrs={'class': 'form-control', 'id': 'title_ru', 'placeholder': 'Название задачи [ru]'}),
            "title_en": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи [en]'}),
            "slug": TextInput(attrs={'class': 'form-control', 'id': 'slug', 'placeholder': 'ссылка'}),
            "content": forms.CharField(widget=CKEditorWidget()),
            "content_ru": forms.CharField(widget=CKEditorWidget()),
            "content_en": forms.CharField(widget=CKEditorWidget()),
            "rubric": Select(attrs={'class': 'form-control', 'placeholder': 'Категория задачи'}),
            "image": FileInput(attrs={'class': 'form-control', 'placeholder': 'Изображение задачи'}),
        }

