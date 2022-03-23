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
    file = models.ImageField()
    music = models.ForeignKey("Music", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Music(core_models.TimeStampedModel):

    """Music Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    price = models.IntegerField()
    music_type = models.ForeignKey("MusicType", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
