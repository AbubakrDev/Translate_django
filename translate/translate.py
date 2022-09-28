from modeltranslation.translator import register , TranslationOptions
from .models import TranslatePage

@register(TranslatePage)
class MalumotTranslateOption(TranslateOptions):
    fields = ('name' , 'title',)