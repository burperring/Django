from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    critic_score = models.IntegerField()
    user_score = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.music}"
