from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Funding
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"
    context_object_name = "fundings"


class FundingDetail(DetailView):

    """FundingDetail Definition"""

    model = models.Funding


def search(request):
    music = request.GET.get("music", "Anywhere")
    # music = str.capitalize(music)
    country = request.GET.get("country", "KR")

    form = {
        "music": music,
        "s_country": country,
    }

    choices = {
        "countries": countries,
    }

    return render(request, "fundings/search.html", {**form, **choices})
