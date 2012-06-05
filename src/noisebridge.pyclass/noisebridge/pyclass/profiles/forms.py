from django import forms
from django.contrib.auth.models import User

from pyclass.fields import CommaSeparatedCharField
from pyclass.profiles.models import UserProfile


class SearchForm(forms.Form):
    query = forms.CharField(max_length=300,
                            label='Enter search term')
    query_type = forms.ChoiceField(choices=(("interest", "Interest"), ("user", "User"),),
                                   label='Specify type of search')


class AddInterestForm(forms.Form):
    interests = CommaSeparatedCharField(max_length=300)


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class UserProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("avatar", "biography")
