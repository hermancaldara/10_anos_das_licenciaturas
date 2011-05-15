from django import forms
from models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        widgets = {
            'poster_abstract': forms.Textarea(attrs={'cols': 60, 'rows': 20}),
        }

