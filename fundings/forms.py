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


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        funding = models.Funding.objects.get(pk=pk)
        photo.funding = funding
        photo.save()


class CreateFundingForm(forms.ModelForm):
    class Meta:
        model = models.Funding
        fields = (
            "name",
            "description",
            "country",
            "price",
            "funding_start",
            "funding_end",
            "music_stock",
            "music_share",
            "music_type",
        )
