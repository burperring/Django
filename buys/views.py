from django.contrib import messages
from django.views.generic import FormView
from django.shortcuts import redirect, reverse
from users import mixins as user_mixins
from fundings import models as funding_models
from django.views.generic import TemplateView
from . import forms


class BuyFundingView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.BuyFundingForm
    template_name = "buys/funding_buy.html"

    def form_valid(self, form):
        str_list = list(self.kwargs.values())
        int_list = list(map(int, str_list))
        funding = funding_models.Funding.objects.get_or_none(pk=int_list[0])
        buy = form.save()
        buy.user = self.request.user
        buy.funding = funding
        buy.save()
        funding.music_share = funding.music_share - buy.buy_share
        funding.save()
        messages.success(self.request, "Buy Funding")
        return redirect(reverse("fundings:detail", kwargs={"pk": funding.pk}))


class SeeMyBuyFunding(TemplateView):

    template_name = "buys/buy_detail.html"
