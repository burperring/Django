from django import forms
from . import models


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        music = models.Music.objects.get(pk=pk)
        photo.music = music
        photo.save()


class CreateMusicForm(forms.ModelForm):
    class Meta:
        model = models.Music
        fields = (
            "name",
            "description",
            "music_type",
        )

    def save(self, *args, **kwargs):
        music = super().save(commit=False)
        return music
