from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    fundings = models.ManyToManyField("fundings.Funding", blank=True)

    def __str__(self):
        return self.name
