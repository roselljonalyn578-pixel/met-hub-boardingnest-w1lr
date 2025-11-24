from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'url', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }