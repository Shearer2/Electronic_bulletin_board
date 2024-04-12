from django.forms import ModelForm

from .models import Bb


class BbForm(ModelForm):
    class Meta:
        model = Bb
        # Указываем поля, которые будут отображаться на форме.
        fields = ('title', 'content', 'price', 'rubric')

