from django.http import Http404
from django.views.generic import DetailView, UpdateView, FormView
from django.shortcuts import redirect, reverse
from users import mixins as user_mixins
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from . import models, forms

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


class EditPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    model = models.Photo
    template_name = "musics/music_photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        music_pk = self.kwargs.get("music_pk")
        return reverse("musics:photos", kwargs={"pk": music_pk})


class AddPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, FormView):

    model = models.Photo
    template_name = "musics/music_photo_create.html"
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("musics:photos", kwargs={"pk": pk}))


class CreateMusicView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateMusicForm
    template_name = "musics/music_create.html"

    def form_valid(self, form):
        music = form.save()
        music.lyricist = self.request.user
        music.save()
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("musics:mdetail", kwargs={"pk": music.pk}))
