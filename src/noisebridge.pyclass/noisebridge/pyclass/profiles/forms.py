from django import forms


class SearchInterestForm(forms.Form):
    query = forms.CharField(max_length=300)


class AddInterestForm(forms.Form):
    interest = forms.CharField(max_length=300)
