from django import forms


class SpecialRequesstForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-floating'}))
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(self.name, self.message)
        # send email using the self.cleaned_data dictionary
        pass
