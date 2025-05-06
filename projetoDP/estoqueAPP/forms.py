from django import forms
from .models import EstoqueModel


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = EstoqueModel
        fields = ["nome", "descricao", "em_estoque"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "em_estoque": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
