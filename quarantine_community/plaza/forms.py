from django import forms

from plaza.models import SpecialRequest


class SpecialRequestForm(forms.ModelForm):
    class Meta:
        model = SpecialRequest
        fields = ('title', 'name', 'responder', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'First Name'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'responder': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }
