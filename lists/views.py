from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from musics import models as music_models
from . import models


def toggle_music(request, music_pk):
    action = request.GET.get("action", None)
    music = music_models.Music.objects.get_or_none(pk=music_pk)
    if music is not None and action is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favorite Musics"
        )
        if action == "add":
            the_list.musics.add(music)
        elif action == "remove":
            the_list.musics.remove(music)
    return redirect(reverse("musics:mdetail", kwargs={"pk": music_pk}))


class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"
