from django.views.generic import ListView, DetailView, View, UpdateView
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Funding
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "fundings"


class FundingDetail(DetailView):

    """FundingDetail Definition"""

    model = models.Funding


class SearchView(View):

    """SearchView Definition"""

    def get(self, request):

        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                name = form.cleaned_data.get("name")
                country = form.cleaned_data.get("country")
                music_type = form.cleaned_data.get("music_type")

                filter_args = {}

                if name != "Anything":
                    filter_args["name__startswith"] = name

                filter_args["country"] = country

                fundings = models.Funding.objects.filter(**filter_args)

                for mt in music_type:
                    fundings = fundings.filter(music_type=mt)

                qs = fundings.order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                fundings = paginator.get_page(page)

                return render(
                    request,
                    "fundings/search.html",
                    {"form": form, "fundings": fundings},
                )

        else:
            form = forms.SearchForm()

        return render(request, "fundings/search.html", {"form": form})


class EditFundingView(UpdateView):

    model = models.Funding
    template_name = "fundings/funding_edit.html"
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
