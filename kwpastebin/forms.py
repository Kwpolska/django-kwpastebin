from django import forms
from kwpastebin.models import LANGUAGE_CHOICES, DEFAULT_LANG

class PasteForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'margin-bottom: 0.5em;', 'placeholder': 'Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'font-family: Consolas, monospace; margin-bottom: 0.5em'}))
    language = forms.ChoiceField(label="Language", choices=LANGUAGE_CHOICES, initial=DEFAULT_LANG, widget=forms.Select(attrs={'class': 'form-control', 'style': 'display: inline; width: auto'}))
    public = forms.BooleanField(label="Public", required=False)