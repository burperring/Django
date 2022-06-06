from django.views.generic import DetailView, UpdateView
from . import models

# Create your views here.


class MusicDetail(DetailView):

    """MusicDetail Definition"""

    model = models.Music


class EditMusicView(UpdateView):

    model = models.Music
    template_name = "musics/music_edit.html"
    fields = (
        "name",
        "description",
        "music_type",
    )
