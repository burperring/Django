from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    list_display = (
        "funding",
        "status",
        "funding_start",
        "funding_end",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
