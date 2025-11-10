from django import forms
from .models import Step101

class Step101Form(forms.ModelForm):
    description = forms.CharField(
        label='Дискрипшн',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    class Meta:
        model = Step101
        fields = ['title', 'h1', 'subtitle', 'brands', 'keyword', 'keywords', 'description', 'seo_description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'h1': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'brands': forms.TextInput(attrs={'class': 'form-control'}),
            'keyword': forms.TextInput(attrs={'class': 'form-control'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'seo_description': forms.TextInput(attrs={'class': 'form-control'}),
        }
