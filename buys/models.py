from django.db import models
from core import models as core_models
from fundings import models as fundiing_models


class Buy(core_models.TimeStampedModel):

    """Buy Model Definition"""

    user = models.ForeignKey(
        "users.User", related_name="buys", on_delete=models.CASCADE
    )
    funding = models.ForeignKey(
        "fundings.Funding", related_name="buys", on_delete=models.CASCADE
    )
    buy_share = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.funding}"

    def buy_funding_share(self):
        funding_share = fundiing_models.Funding.objects.music_share()
        # funding_share = funding_share - self.buy_share
        return funding_share
