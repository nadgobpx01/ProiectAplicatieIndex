from django import forms
from .models import Consumption

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = ['tip', 'furnizor', 'index_nou', 'unitate_masura', 'pret_unitar']
        widgets = {
            'tip': forms.Select(attrs={'class': 'form-select'}),
            'furnizor': forms.TextInput(attrs={'class': 'form-control'}),
            'index_nou': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unitate_masura': forms.TextInput(attrs={'class': 'form-control'}),
            'pret_unitar': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
