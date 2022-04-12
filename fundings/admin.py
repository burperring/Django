from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(
    models.MusicType,  # models.Facility, models.Amenity, models.HouseRule
)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.fundings.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Funding)
class FundingAdmin(admin.ModelAdmin):

    """Funding Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "lyricist", "description", "price")},
        ),
        (
            "Times",
            {"fields": ("funding_start", "funding_end")},
        ),
        (
            "Spaces",
            {"fields": ("music_type", "music_stock", "music_share")},
        ),
        # (
        #    "More About the Space",
        #    {
        #        "classes": ("collapse",),
        #        "fields": ("amenities", "facilities", "house_rules"),
        #    },
        # ),
        # (
        #    "Last Details",
        #    {"fields": ("host",)},
        # ),
    )

    list_display = (
        "name",
        "lyricist",
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

    # list_filter = (
    #    "instant_book",
    #    "host__superhost",
    #    "music_type",
    #    "amenities",
    #    "facilities",
    #    "house_rules",
    #    "city",
    #    "country",
    # )

    raw_id_fields = ("lyricist",)

    search_fields = (
        # "=city",
        "^host__username",
    )

    filter_horizontal = ("music_type",)

    # def count_amenities(self, obj):
    #    return obj.amenities.count()

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
