from django.contrib import admin
from . import models


@admin.register(models.MusicType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Funding)
class FundingAdmin(admin.ModelAdmin):

    """Music Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """"""

    pass
