from django import forms
from pyclass.profiles.models import Interest


class SearchInterestForm(forms.Form):
    query = forms.CharField(max_length=300)

class AddInterestForm(forms.Form):
    interest = forms.CharField(max_length=300)

    def clean_interest(self):
        interest = self.cleaned_data["interest"]
        interest_list = Interest.objects.filter(name=interest).count()
        if interest_list:
            raise forms.ValidationError("Interest already exists!")
        return interest
