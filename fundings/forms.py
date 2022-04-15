from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    name = forms.CharField(initial="Anything")
    country = CountryField(default="KR").formfield()
    music_type = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.MusicType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
