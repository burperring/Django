from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
from core import models as core_models
from cal import Calendar


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MusicType(AbstractItem):

    """MusicType Model Definition"""

    class Meta:
        verbose_name = "Music Type"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="funding_photos")
    funding = models.ForeignKey(
        "Funding", related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class song(core_models.TimeStampedModel):

    """song Model Definition"""

    caption = models.CharField(max_length=80)
    sfile = models.FileField(upload_to="musics/")
    funding = models.ForeignKey(
        "Funding", related_name="songs", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class Funding(core_models.TimeStampedModel):

    """Funding Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    price = models.IntegerField()
    funding_start = models.DateField()
    funding_end = models.DateField()
    music_stock = models.IntegerField()
    music_share = models.IntegerField()
    lyricist = models.ForeignKey(
        "users.User", related_name="fundings", on_delete=models.CASCADE
    )
    music_type = models.ManyToManyField(
        "MusicType", related_name="fundings", blank=True
    )

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #    self.city = str.capitalize(self.city)
    #    super().save(*args, **kwargs)

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.funding_start and now <= self.funding_end

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.funding_end

    is_finished.boolean = True

    def share_price(self):
        share_price = self.price / self.music_stock
        return round(share_price, 2)

    def get_absolute_url(self):
        return reverse("fundings:detail", kwargs={"pk": self.pk})

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_photo(self):
        try:
            (photo,) = self.photos.all()[1:2]
            return photo.file.url
        except ValueError:
            return None

    def get_calendars(self):
        this_month = Calendar(2022, 6)
        next_month = Calendar(2022, 7)
        return (this_month, next_month)
