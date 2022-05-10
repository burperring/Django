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


@admin.register(models.Funding)
class FundingAdmin(admin.ModelAdmin):

    """Funding Admin Definition"""

    inlines = (
        PhotoInline,
        songline,
    )

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "lyricist", "country", "description", "price")},
        ),
        (
            "Times",
            {"fields": ("funding_start", "funding_end")},
        ),
        (
            "Spaces",
            {"fields": ("music_type", "music_stock", "music_share")},
        ),
    )

    list_display = (
        "name",
        "lyricist",
        "country",
        "price",
        "music_stock",
        "music_share",
        "share_price",
        "funding_start",
        "funding_end",
        "in_progress",
        "is_finished",
        "count_photos",
    )

    raw_id_fields = ("lyricist",)

    search_fields = ("^lyricist__username",)

    filter_horizontal = ("music_type",)

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


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
