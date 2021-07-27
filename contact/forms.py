from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("email", "name", "firstname", "phone", "text", "image")
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваш Email..."}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя..."}),
            "firstname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваша фамилия..."}),
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Ваше обращение ..."}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваш телефон..."}),
            "image": forms.FileInput(attrs={"class": "form-control", "before": "согласен..."}),

        }
        labels = {
            "email": 'ssss',
            "name": '',
            "firstname": '',
            "phone": '',
            "text": '',
            "file_obj": '',
        }
