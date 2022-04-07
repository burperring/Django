from django.shortcuts import render
from . import models


def all_fundings(request):
    all_fundings = models.Funding.objects.all()
    return render(
        request, "fundings/all_fundings.html", context={"fundings": all_fundings}
    )
