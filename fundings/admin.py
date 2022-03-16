from django.contrib import admin
from . import models


@admin.register(models.Funding)
class FundingAdmin(admin.ModelAdmin):

    pass
