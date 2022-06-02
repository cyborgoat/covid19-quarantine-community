from django import forms

from plaza.models import SpecialRequest, SupplyRegistration, SupplyItem, CountryYard, BuildingUnit, \
    DrinkingWaterRegistration


class SpecialRequestForm(forms.ModelForm):
    class Meta:
        model = SpecialRequest
        fields = ('title', 'country_yard', 'building_unit', 'building_subunit', 'room_num', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control input-lg', 'placeholder': '输入主题'}),
            'country_yard': forms.Select(attrs={'class': 'form-select'}),
            'building_unit': forms.Select(attrs={'class': 'form-select'}),
            'building_subunit': forms.Select(attrs={'class': 'form-select'}),
            'room_num': forms.TextInput(
                attrs={'class': 'form-control input-lg', 'placeholder': '请输入房间号'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }

    def __init__(self, *args, **kwargs):
        super(SpecialRequestForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "主题"
        self.fields['country_yard'].label = "所属院"
        self.fields['building_unit'].label = "所属楼号"
        self.fields['building_subunit'].label = "所属单元(不涉及请选择0单元)"
        self.fields['room_num'].label = "房间号"
        self.fields['body'].label = "详细信息"


class SupplyRegistrationForm(forms.ModelForm):
    class Meta:
        model = SupplyRegistration
        fields = ('country_yard', 'building_unit', 'building_subunit', 'room_num', 'items')

        widgets = {
            'country_yard': forms.Select(attrs={'class': 'form-select'}),
            'building_unit': forms.Select(attrs={'class': 'form-select'}),
            'building_subunit': forms.Select(attrs={'class': 'form-select'}),
            'room_num': forms.TextInput(
                attrs={'class': 'form-control input-lg', 'placeholder': '请输入房间号'}),
            'items': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        }

    def __init__(self, *args, **kwargs):
        super(SupplyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['country_yard'].label = "所属院"
        self.fields['building_unit'].label = "所属楼号"
        self.fields['building_subunit'].label = "所属单元(不涉及请选择0单元)"
        self.fields['room_num'].label = "房间号"
        self.fields['items'].label = "所需物品"


class DrinkingWaterRegistrationForm(forms.ModelForm):
    class Meta:
        model = DrinkingWaterRegistration
        fields = ('country_yard', 'building_unit', 'building_subunit', 'room_num')

        widgets = {
            'country_yard': forms.Select(attrs={'class': 'form-select'}),
            'building_unit': forms.Select(attrs={'class': 'form-select'}),
            'building_subunit': forms.Select(attrs={'class': 'form-select'}),
            'room_num': forms.TextInput(
                attrs={'class': 'form-control input-lg', 'placeholder': '请输入房间号'}),
        }

    def __init__(self, *args, **kwargs):
        super(DrinkingWaterRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['country_yard'].label = "所属院"
        self.fields['building_unit'].label = "所属楼号"
        self.fields['building_subunit'].label = "所属单元(不涉及请选择0单元)"
        self.fields['room_num'].label = "房间号"
