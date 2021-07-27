from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Sovet)
class SovetTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )

@register(Chelensoveta)
class ChelensovetaTranslationOptions(TranslationOptions):
    fields = ('title', 'doljnost', 'works',)
