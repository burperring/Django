from django.contrib import admin
from . import models


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """"""

    pass


@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):

    """Music Admin Definition"""

    list_display = (
        "name",
        "description",
        "price",
        "total_rating",
    )
