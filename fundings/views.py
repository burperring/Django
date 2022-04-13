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
    name = request.GET.get("name", "Anything")
    # music = str.capitalize(music)
    country = request.GET.get("country", "KR")
    s_music_types = request.GET.getlist("music_types")

    form = {
        "name": name,
        "s_country": country,
        "s_music_types": s_music_types,
    }

    music_types = models.MusicType.objects.all()

    choices = {
        "countries": countries,
        "music_types": music_types,
    }

    filter_args = {}

    if name != "Anything":
        filter_args["name__startswith"] = name

    filter_args["country"] = country

    fundings = models.Funding.objects.filter(**filter_args)

    return render(
        request, "fundings/search.html", {**form, **choices, "fundings": fundings}
    )
