from django import forms
from .models import News

class NewsSelectionForm(forms.Form):
    selected_news = forms.ModelMultipleChoiceField(
        queryset=News.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )