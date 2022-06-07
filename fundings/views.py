from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from . import models, forms


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Funding
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "fundings"


class FundingDetail(DetailView):

    """FundingDetail Definition"""

    model = models.Funding


class SearchView(View):

    """SearchView Definition"""

    def get(self, request):

        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                name = form.cleaned_data.get("name")
                country = form.cleaned_data.get("country")
                music_type = form.cleaned_data.get("music_type")

                filter_args = {}

                if name != "Anything":
                    filter_args["name__startswith"] = name

                filter_args["country"] = country

                fundings = models.Funding.objects.filter(**filter_args)

                for mt in music_type:
                    fundings = fundings.filter(music_type=mt)

                qs = fundings.order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                fundings = paginator.get_page(page)

                return render(
                    request,
                    "fundings/search.html",
                    {"form": form, "fundings": fundings},
                )

        else:
            form = forms.SearchForm()

        return render(request, "fundings/search.html", {"form": form})


class EditFundingView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Funding
    template_name = "fundings/funding_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "price",
        "funding_start",
        "funding_end",
        "music_stock",
        "music_share",
        "music_type",
    )

    def get_object(self, queryset=None):
        funding = super().get_object(queryset=queryset)
        if funding.lyricist.pk != self.request.user.pk:
            raise Http404()
        return funding


class FundingPhotosView(user_mixins.LoggedInOnlyView, DetailView):

    model = models.Funding
    template_name = "fundings/funding_photos.html"

    def get_object(self, queryset=None):
        funding = super().get_object(queryset=queryset)
        if funding.lyricist.pk != self.request.user.pk:
            raise Http404()
        return funding


@login_required
def delete_photo(request, funding_pk, photo_pk):
    user = request.user
    try:
        funding = models.Funding.objects.get(pk=funding_pk)
        if funding.lyricist.pk != user.pk:
            messages.error(request, "Can't delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Delete")
        return redirect(reverse("fundings:photos", kwargs={"pk": funding_pk}))
    except models.Funding.DoesNotExist:
        return redirect(reverse("core:home"))


class EditPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    model = models.Photo
    template_name = "fundings/funding_photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        funding_pk = self.kwargs.get("funding_pk")
        return reverse("fundings:photos", kwargs={"pk": funding_pk})


class AddPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, FormView):

    model = models.Photo
    template_name = "fundings/funding_photo_create.html"
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("fundings:photos", kwargs={"pk": pk}))


class UploadFundingView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateFundingForm
    template_name
