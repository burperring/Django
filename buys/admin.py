from django.contrib import admin
from . import models


@admin.register(models.Buy)
class BuyAdmin(admin.ModelAdmin):

    """Buy Admin Definition"""

    list_display = (
        "user",
        "funding",
        "buy_share",
    )

    search_fields = ("user",)
