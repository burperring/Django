from django import forms
from . import models


class BuyFundingForm(forms.ModelForm):
    class Meta:
        model = models.Buy
        fields = ("buy_share",)

    def save(self):
        buy = super().save(commit=False)
        return buy
