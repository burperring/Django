from django.db import models
from django.urls import reverse
from django.utils import timezone

# from django_countries.fields import CountryField
from core import models as core_models


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


# class Amenity(AbstractItem):
#
#    """Amenity Model Definition"""
#
#    class Meta:
#        verbose_name_plural = "Amenities"


# class Facility(AbstractItem):
#
#    """Facility Model Definition"""
#
#    class Meta:
#        verbose_name_plural = "Facilities"


# class HouseRule(AbstractItem):
#
#    """HouseRule Model Definition"""
#
#    class Meta:
#        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="funding_photos")
    funding = models.ForeignKey(
        "Funding", related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class Funding(core_models.TimeStampedModel):

    """Funding Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    # country = CountryField()
    # city = models.CharField(max_length=80)
    price = models.IntegerField()
    # address = models.CharField(max_length=140)
    # guests = models.IntegerField()
    # beds = models.IntegerField()
    # bedrooms = models.IntegerField()
    # baths = models.IntegerField()
    # check_in = models.DateField()
    # check_out = models.DateField()
    funding_start = models.DateField()
    funding_end = models.DateField()
    # instant_book = models.BooleanField(default=False)
    music_stock = models.IntegerField()
    music_share = models.IntegerField()
    lyricist = models.ForeignKey(
        "users.User", related_name="fundings", on_delete=models.CASCADE
    )
    music_type = models.ManyToManyField(
        "MusicType", related_name="fundings", blank=True
    )
    # amenities = models.ManyToManyField("Amenity", related_name="fundings", blank=True)
    # facilities = models.ManyToManyField("Facility", related_name="fundings", blank=True)
    # house_rules = models.ManyToManyField(
    #    "HouseRule", related_name="fundings", blank=True
    # )

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #    self.city = str.capitalize(self.city)  # 대문자 생성
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
        return share_price

    def get_absolute_url(self):
        return reverse("fundings:detail", kwargs={"pk": self.pk})
