from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, SelectMultiple, CheckboxInput
from .models import Comment, Post, Category, Tag


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ['text']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['status', 'author','yved', 'title_en', 'title_ru', 'slug', 'content_ru', 'content_en', 'category', 'tags', 'image',]

        widgets = {
            "author": Select(attrs={'class': 'form-control', 'placeholder': 'автор статьи'}),

            "status": Select(attrs={'class': 'form-control', 'placeholder': 'Статус статьи'}),
            "yved": CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Уведомить'}),
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            "title_ru": TextInput(attrs={'class': 'form-control', 'id': 'title_ru', 'placeholder': 'Название статьи [ru]'}),
            "title_en": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи [en]'}),
            "slug": TextInput(attrs={'class': 'form-control', 'id': 'slug', 'placeholder': 'ссылка'}),
            "content": forms.CharField(widget=CKEditorWidget()),
            "content_ru": forms.CharField(widget=CKEditorWidget()),
            "content_en": forms.CharField(widget=CKEditorWidget()),
            "category": Select(attrs={'class': 'form-control', 'placeholder': 'Категория статьи'}),
            "tags": SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Метки статьи'}),
            "image": FileInput(attrs={'class': 'form-control', 'placeholder': 'Фото статьи'}),
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name_ru', 'slug', 'name_en', 'button', 'image']

        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название метки'}),
            "slug": TextInput(attrs={'class': 'form-control', 'id': 'slug', 'placeholder': 'ссылка'}),
            "name_ru": TextInput(attrs={'class': 'form-control', 'id': 'name_ru', 'placeholder': 'Название метки [ru]'}),
            "name_en": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название метки [en]'}),
            "button": Select(attrs={'class': 'form-control', 'placeholder': 'Статус метки'}),
            "image": FileInput(attrs={'class': 'form-control', 'placeholder': 'Фото метки'}),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name_ru', 'name_en', 'slug', 'parent']

        widgets = {
            "parent": Select(attrs={'class': 'form-control', 'placeholder': 'Родитель'}),
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название категории'}),
            "name_ru": TextInput(attrs={'class': 'form-control', 'id': 'name_ru', 'placeholder': 'Название  категории [ru]'}),
            "name_en": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название категории [ru]'}),
            "slug": TextInput(attrs={'class': 'form-control', 'id': 'slug', 'placeholder': 'ссылка'}),
        }

