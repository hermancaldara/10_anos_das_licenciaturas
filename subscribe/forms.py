from django import forms
from models import Entry
from django.contrib.localflavor.br.forms import BRCPFField, BRPhoneNumberField


class EntryForm(forms.ModelForm):
    
    phone = BRPhoneNumberField(label="Telefone", help_text="Exemplo: XX-XXXX-XXXX")
    mobile = BRPhoneNumberField(label="Celular", help_text="Exemplo: XX-XXXX-XXXX")
    cpf = BRCPFField(label="CPF", help_text="Exemplo: XXX.XXX.XXX-VD")
    
    class Meta:
        model = Entry
        widgets = {
            'poster_abstract': forms.Textarea(attrs={'cols': 54, 'rows': 20}),
        }

