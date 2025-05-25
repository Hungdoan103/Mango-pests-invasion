from django import forms
from .models import SurveillanceSession

class SurveillanceSessionForm(forms.ModelForm):
    class Meta:
        model = SurveillanceSession
        fields = ['name', 'total_plants', 'confidence_level', 'error_margin', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'total_plants': forms.NumberInput(attrs={'class': 'form-control'}),
            'confidence_level': forms.NumberInput(attrs={'class': 'form-control', 'min': '0.8', 'max': '0.99', 'step': '0.01'}),
            'error_margin': forms.NumberInput(attrs={'class': 'form-control', 'min': '0.01', 'max': '0.1', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
