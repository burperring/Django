from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_fundings(request):
    page = request.GET.get("page")
    funding_list = models.Funding.objects.all()
    paginator = Paginator(funding_list, 10)
    fundings = paginator.get_page(page)
    return render(
        request,
        "fundings/all_fundings.html",
        {"fundings": fundings},
    )
