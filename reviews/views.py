from django.contrib import messages
from django.views.generic import FormView
from django.shortcuts import redirect, reverse
from users import mixins as user_mixins
from musics import models as music_models
from . import forms


class CreateReviewView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateReviewForm
    template_name = "musics/music_review.html"

    def form_valid(self, form):
        music = music_models.Music.objects.get_or_none(pk=self.pk)
        review = form.save()
        review.user = self.request.user
        review.save()
        form.save_m2m()
        messages.success(self.request, "Review Uploaded")
        return redirect(reverse("music:mdetail", kwargs={"music": music.pk}))


# class CreateReviewView(user_mixins.LoggedInOnlyView, FormView):

#   form_class = forms.CreateReviewForm
#   template_name = "musics/music_review.html"

#    def form_valid(self, form):
#        review = form.save()
#        review.user = self.request.user
#        review.save()
#        form.save_m2m()
#        messages.success(self.request, "Review Uploaded")
#        return redirect(reverse("music:mdetail", kwargs={"music": review.music}))
