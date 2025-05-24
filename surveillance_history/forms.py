from django import forms
from django.forms import formset_factory
from .models import SurveillanceHistory, PestDetection, DiseaseDetection

class SurveillanceHistoryForm(forms.ModelForm):
    class Meta:
        model = SurveillanceHistory
        fields = ['plants_checked', 'plants_with_pests', 'plants_with_diseases']
        widgets = {
            'plants_checked': forms.NumberInput(attrs={'class': 'form-control'}),
            'plants_with_pests': forms.NumberInput(attrs={'class': 'form-control'}),
            'plants_with_diseases': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PestDetectionForm(forms.ModelForm):
    class Meta:
        model = PestDetection
        fields = ['pest_name', 'count', 'severity', 'notes']
        widgets = {
            'pest_name': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class DiseaseDetectionForm(forms.ModelForm):
    class Meta:
        model = DiseaseDetection
        fields = ['disease_name', 'count', 'severity', 'notes']
        widgets = {
            'disease_name': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
