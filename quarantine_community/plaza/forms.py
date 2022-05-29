from django import forms

from plaza.models import SpecialRequest, SupplyRegistration, SupplyItem, CountryYard, BuildingUnit


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


class SupplyRegistrationForm(forms.ModelForm):
    class Meta:
        model = SupplyRegistration
        fields = ('country_yard', 'building_unit', 'room_num', 'items')

        widgets = {
            'country_yard': forms.Select(attrs={'class': 'form-control'}),
            'building_unit': forms.Select(attrs={'class': 'form-control'}),
            'room_num': forms.TextInput(
                attrs={'class': 'form-control input-lg', 'placeholder': 'Enter Room Number'}),
            'items': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        }

    def __init__(self, *args, **kwargs):
        super(SupplyRegistrationForm, self).__init__(*args, **kwargs)
        # self.fields['items'].label = False
