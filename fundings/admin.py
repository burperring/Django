from django.contrib import admin
from . import models


@admin.register(models.MusicType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Funding)
class FundingAdmin(admin.ModelAdmin):

    pass
