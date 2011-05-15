from django import forms
from models import Entry
from django.contrib.localflavor.br.forms import BRCPFField, BRPhoneNumberField


class EntryForm(forms.ModelForm):
    
    cpf = BRCPFField(help_text="Exemplo: XXX.XXX.XXX-VD")
    phone = BRPhoneNumberField(help_text="Exemplo: XX-XXXX-XXXX")
    mobile = BRPhoneNumberField(help_text="Exemplo: XX-XXXX-XXXX")
    
    class Meta:
        model = Entry
        widgets = {
            'poster_abstract': forms.Textarea(attrs={'cols': 54, 'rows': 20}),
        }

