from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=300,
                            label='Enter search term')
    query_type = forms.ChoiceField(choices=(("interest", "Interest"), ("user", "User"),),
                                   label='Specify type of search')


class AddInterestForm(forms.Form):
    interest = forms.CharField(max_length=300)
