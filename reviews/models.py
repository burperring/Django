from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    critic_score = models.IntegerField()
    user_score = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    music = models.ForeignKey(
        "musics.Music", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.music}"

    def rating_average(self):
        avg = (self.critic_score + self.user_score) / 2
        return round(avg, 2)

    rating_average.short_description = "Avg"
