from django.http import Http404
from django.views.generic import DetailView, UpdateView
from django.shortcuts import redirect, reverse
from users import mixins as user_mixins
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models

# Create your views here.


class MusicDetail(DetailView):

    """MusicDetail Definition"""

    model = models.Music


class EditMusicView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Music
    template_name = "musics/music_edit.html"
    fields = (
        "name",
        "description",
        "music_type",
    )

    def get_object(self, queryset=None):
        music = super().get_object(queryset=queryset)
        if music.lyricist.pk != self.request.user.pk:
            raise Http404()
        return music


class MusicPhotosView(user_mixins.LoggedInOnlyView, DetailView):

    model = models.Music
    template_name = "musics/music_photos.html"

    def get_object(self, queryset=None):
        music = super().get_object(queryset=queryset)
        if music.lyricist.pk != self.request.user.pk:
            raise Http404()
        return music


@login_required
def delete_photo(request, music_pk, photo_pk):
    user = request.user
    try:
        music = models.Music.objects.get(pk=music_pk)
        if music.lyricist.pk != user.pk:
            messages.error(request, "Can't delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Delete")
        return redirect(reverse("musics:photos", kwargs={"pk": music_pk}))
    except models.Music.DoesNotExist:
        return redirect(reverse("core:home"))
