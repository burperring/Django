from django.shortcuts import render
from . import models


def all_fundings(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_fundings = models.Funding.objects.all()[offset:limit]
    return render(
        request, "fundings/all_fundings.html", context={"fundings": all_fundings}
    )
