from django.db import models
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    funding_start = models.DateField()
    funding_end = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    funding = models.ForeignKey("fundings.Funding", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.funding} - {self.funding_start}"
