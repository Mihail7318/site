from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Smena)
class SmenaTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
