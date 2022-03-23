from django.contrib import admin
from . import models


@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):

    """Music Admin Definition"""

    pass
