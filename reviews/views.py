from django.contrib import messages
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import FormView
from django.shortcuts import redirect, reverse
from users import mixins as user_mixins
from musics import models as music_models
from . import forms


class CreateReviewView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateReviewForm
    template_name = "musics/music_review.html"

    def form_valid(self, form):
        str_list = list(self.kwargs.values())
        int_list = list(map(int, str_list))
        music = music_models.Music.objects.get_or_none(pk=int_list[0])
        review = form.save()
        review.user = self.request.user
        review.music = music
        review.save()
        messages.success(self.request, "Review Uploaded")
        return redirect(reverse("musics:mdetail", kwargs={"pk": music.pk}))


# def create_review(request, music):
#    if request.method == "POST":
#        form = forms.CreateReviewForm(request.POST)
#        music = music_models.Music.objects.get_or_none(pk=music)
#        if not music:
#            return redirect(reverse("core:home"))
#        if form.is_valid():
#            review = form.save()
#            review.music = music
#            review.user = request.user
#            review.save()
#            messages.success(request, "Music Reviewed")
#            return redirect(reverse("musics:mdetail", kwargs={"pk": music.pk}))
