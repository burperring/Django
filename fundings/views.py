from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_fundings(request):
    page = request.GET.get("page", 1)
    funding_list = models.Funding.objects.all()
    paginator = Paginator(funding_list, 10, orphans=3)
    try:
        fundings = paginator.page(int(page))
        return render(
            request,
            "fundings/all_fundings.html",
            {"page": fundings},
        )
    except EmptyPage:
        fundings = paginator.page(1)
        return redirect("/")
