from django.contrib import admin
from . import models


@admin.register(models.MusicType)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):

    """Music Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """"""

    pass
