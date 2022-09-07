from django import forms
from .models import Section


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'note1', 'note2', 'note3']
