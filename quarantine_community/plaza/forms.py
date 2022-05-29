from django import forms

from plaza.models import SpecialRequest


class SpecialRequestForm(forms.ModelForm):
    class Meta:
        model = SpecialRequest
        fields = ('title', 'name', 'responder', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control input-lg', 'placeholder': 'Enter Title'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'responder': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Report your responder'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }
