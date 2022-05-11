from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.MusicType)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.fundings.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


class songline(admin.TabularInline):

    model = models.song


@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):

    """Music Admin Definition"""

    inlines = (
        PhotoInline,
        songline,
    )

    list_display = (
        "name",
        "lyricist",
        "description",
        "price",
        "total_rating",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    filter_horizontal = ("music_type",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.song)
class songAdmin(admin.ModelAdmin):

    """song Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(
            f'<audio controls><source src="{obj.sfile.url}"type"audio/mpeg"></audio>'
        )

    get_thumbnail.short_description = "play"
