from django.views.generic import DetailView
from . import models

# Create your views here.


class MusicDetail(DetailView):

    """MusicDetail Definition"""

    model = models.Music
