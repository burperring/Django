from django.db import models
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


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="music_photos")
    music = models.ForeignKey("Music", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class song(core_models.TimeStampedModel):

    """song Model Definition"""

    caption = models.CharField(max_length=80)
    sfile = models.FileField(upload_to="musics/")
    music = models.ForeignKey("Music", related_name="songs", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Music(core_models.TimeStampedModel):

    """Music Model Definition"""

    name = models.CharField(max_length=140)
    lyricist = models.ForeignKey(
        "users.User", related_name="musics", on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.IntegerField()
    music_type = models.ManyToManyField("MusicType", related_name="musics", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0
