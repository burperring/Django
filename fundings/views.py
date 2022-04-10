from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Funding
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"
    context_object_name = "fundings"


def funding_detail(request, pk):
    try:
        funding = models.Funding.objects.get(pk=pk)
        return render(request, "fundings/detail.html", {"funding": funding})
    except models.Funding.DoesNotExist:
        return redirect(reverse("core:home"))
