from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Funding
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"
    context_object_name = "fundings"
